<img width="1826" height="1552" alt="image" src="https://github.com/user-attachments/assets/a02d31c7-700f-4c51-a18d-0e3fc79a4414" />

# Movie Recommender System

A simple movie recommendation web application built with Python, Flask, and Pandas.  
Users can search for a movie title and receive recommendations based on collaborative filtering and correlation between user ratings.

---

# Features

- Search movies by title
- Automatically matches similar movie names
- Displays recommended movies based on user rating similarity
- Web-based UI using Flask
- Uses the MovieLens dataset

---

# How Movie Matching Works

The application allows users to search using partial movie titles instead of requiring the exact dataset title.

For example:

- `Toy Story`
- `star wars`
- `fargo`

will successfully match:

- `Toy Story (1995)`
- `Star Wars (1977)`
- `Fargo (1996)`

This is done using a case-insensitive substring search.


## Matching Process

1. The user enters a movie title into the search bar.
2. The application converts both the user input and dataset titles to lowercase.
3. It checks whether the user input exists inside any movie title.
4. The first matching movie is selected.
5. Recommendations are generated using correlation between user ratings.

---

# Recommendation Algorithm

The recommender system uses collaborative filtering.

## Steps

1. Build a user-movie rating matrix
2. Select ratings for the searched movie
3. Compute correlations with other movies
4. Filter out movies with very few ratings
5. Sort by highest correlation

Movies with higher correlation values are considered more similar.

---

# Technologies Used

- Python
- Flask
- Pandas
- Matplotlib
- Seaborn

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender
```

## Install Dependencies

```bash
pip install flask pandas matplotlib seaborn
```

---

# Running the Application

Start the Flask server:

```bash
python3 app.py


Open in browser:

```text
http://127.0.0.1:5000
```

---

# Dataset Files

Required files:

- `file.tsv`
- `Movie_Id_Titles.csv`

These files should be placed in the project root directory.


# Author

Alexis Newell
