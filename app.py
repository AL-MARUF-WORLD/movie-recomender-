import gradio as gr
import requests
import pandas as pd
import numpy as np

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
        movie_id)
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters


# Load data
movies = pd.read_csv('movie_list.csv')

# Load compressed similarity matrix
similarity_data = np.load('similarity.npz')
similarity = similarity_data['similarity']

# Create movie list for dropdown
movie_list = movies['title'].values

# Gradio interface function
def show_recommendation(selected_movie):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    # Return only images (not tuples)
    return (
        recommended_movie_posters[0],
        recommended_movie_posters[1],
        recommended_movie_posters[2],
        recommended_movie_posters[3],
        recommended_movie_posters[4]
    )


# Create Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# 🎬 Movie Recommender System")

    selected_movie = gr.Dropdown(
        choices=movie_list.tolist(),
        label="Select a Movie"
    )

    btn = gr.Button("Show Recommendation")

    with gr.Row():
        col1 = gr.Image(height=300)
        col2 = gr.Image(height=300)
        col3 = gr.Image(height=300)
        col4 = gr.Image(height=300)
        col5 = gr.Image(height=300)

    btn.click(
        fn=show_recommendation,
        inputs=selected_movie,
        outputs=[col1, col2, col3, col4, col5],
        queue=False
    )

demo.launch()