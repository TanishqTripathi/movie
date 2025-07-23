import streamlit as st
import pickle
import pandas as pd

# Recommend top 5 similar movies
def recommend(movie):
    movie_idx = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_idx]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    
    return recommended_movies

# UI Title
st.title("🎬 Movie Recommendation System")

# Load data
movie_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Movie dropdown
selected_movie = st.selectbox(
    'Select a movie to get recommendations:',
    movies['title'].values
)

# Show recommendations
if st.button('Get Recommendations'):
    recommendations = recommend(selected_movie)
    for name in recommendations:
        st.write("👉", name)
