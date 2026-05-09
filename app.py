from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# ----------------------------
# LOAD DATA
# ----------------------------

column_names = ['user_id', 'item_id', 'rating', 'timestamp']

df = pd.read_csv('file.tsv', sep='\t', names=column_names)
movie_titles = pd.read_csv('Movie_Id_Titles.csv')

data = pd.merge(df, movie_titles, on='item_id')

ratings = pd.DataFrame(data.groupby('title')['rating'].mean())
ratings['num of ratings'] = data.groupby('title')['rating'].count()

moviemat = data.pivot_table(index='user_id',
                            columns='title',
                            values='rating')

# ----------------------------
# HOME PAGE
# ----------------------------

@app.route("/", methods=["GET", "POST"])
def index():

    recommendations = []
    movie = ""

    if request.method == "POST":

        movie = request.form["movie"]

        # Find matching movie titles
        matches = [
            title for title in moviemat.columns
            if movie.lower() in title.lower()
        ]

        if matches:

            # Use first matching movie
            selected_movie = matches[0]

            movie_user_ratings = moviemat[selected_movie]

            similar_to_movie = moviemat.corrwith(movie_user_ratings)

            corr_movie = pd.DataFrame(
                similar_to_movie,
                columns=['Correlation']
            )

            corr_movie.dropna(inplace=True)

            corr_movie = corr_movie.join(
                ratings['num of ratings']
            )

            recommendations = corr_movie[
                corr_movie['num of ratings'] > 10
            ]

            recommendations = recommendations[
                recommendations.index != selected_movie
            ]

            recommendations = recommendations.sort_values(
                'Correlation',
                ascending=False
            ).head(10)

            recommendations = recommendations.reset_index()

            recommendations = recommendations.to_dict(
                orient='records'
            )

            movie = selected_movie
    return render_template(
        "index.html",
        movie=movie,
        tables=recommendations
    )
if __name__ == "__main__":
    app.run(debug=True)