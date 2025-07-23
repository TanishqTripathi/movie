import streamlit as st
import pickle
import pandas as pd
import requests

# def fetch_poster(movie_id):
#     response = requests.get()
    
def recommend(movie):
    movie_idx = movies[movies['title']==movie].index[0]
    distance = similarity[movie_idx]
    movie_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_poster = []
    
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies

st.title("Movie Recommendation System")
movie_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

selected_movie = st.selectbox(
    'Select a movie to get recommendations:',
    movies['title'].values
)

if st.button('Get Recommendations'):
    recommendations = recommend(selected_movie)
    for i in recommendations:
        st.write(i)