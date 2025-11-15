
 # Movie Recommender System

Content-Based Movie Similarity Engine using TMDB Metadata






A production-ready movie recommendation system that predicts 5 movies similar to any selected movie.
Powered by content-based filtering using metadata from the TMDB Movie Dataset.

📂 Dataset

TMDB Movie Metadata
Source: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

## Dataset includes:

Movie title

Overview

Genres

Keywords

Cast & Crew

Popularity & vote data

## Features

🔍 Content-based filtering (metadata-driven)

🧠 Movie vectors built using text feature extraction (Bag-of-Words)

📐 Cosine similarity matrix for recommendations

⚡ Fast predictions using pre-computed .pkl files

🌐 Deployable on HuggingFace Spaces / Streamlit Sharing

🧩 Clean modular code

🚀 Live Demo

(Replace this link when your Space is public)
👉 Live on HuggingFace Spaces: (https://huggingface.co/spaces/AlMARUF69/movie_recommender-1)

🛠️ Installation

Clone the repository:

git clone https://github.com/AL-MARUF-WORLD/movie-recomender

cd movie_recommender


Install dependencies:

pip install -r requirements.txt


Run the app:

python app.py

🧠 System Architecture
Movie-Recommender/
│── app.py                     # UI: Streamlit/Gradio App
│── movie_list.pkl             # Preprocessed movie metadata
│── similarity_compressed.pkl.gz   # Cosine similarity matrix (compressed)
│── requirements.txt
│── README.md
└── .gitattributes

## How It Works (Technical Overview)

Data Preprocessing

Merge movies + credits dataset

Extract: genres, keywords, cast, crew, overview

Convert structured data → cleaned text vector

Vectorization

Build vocabulary using CountVectorizer (max_features=5000)

Generate movie-feature vectors

Similarity Calculation

Apply cosine similarity on vectors

Save similarity matrix as a compressed pickle

Recommendation Logic

def recommend(movie):
    index = movie_list[movie_list['title'] == movie].index[0]
    distances = similarity[index]
    movie_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [movie_list.iloc[i[0]].title for i in movie_indices]

🖼️ Screenshots

(Add your images later)

![UI Screenshot](images/ui.png)
![Recommendation Example](images/result.png)

## Requirements
pandas
numpy
scikit-learn
streamlit / gradio

🧩 Deployment: HuggingFace Spaces

Create a Gradio or Streamlit Space

Upload:

app.py

movie_list.pkl

similarity_compressed.pkl.gz

requirements.txt

Push changes → Space auto-builds

Done! Accessible globally.

📜 License

This project is licensed under the MIT License.

🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss your ideas.

⭐ Support

If you find this project helpful:
👉 Star this repo to support future improvements!
