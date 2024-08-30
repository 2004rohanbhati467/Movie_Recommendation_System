import pandas as pd
import streamlit as st
import pickle
import pandas as pd


with open('movies_list.pkl','rb') as read_file:
    movies = pickle.load(read_file)
movies=pd.DataFrame(movies)

st.title('Movie Recommendation System')
selected_movie_name = st.selectbox(
'Which movie you want to Watch?',movies['title'].values
)

def recommend(movie):
    movie_index = movies[movies['title'] == movie.lower()].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    for i in movies_list:
        # movie_id=i[0]
        #fetch poster from API

        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

similarity = pickle.load(open('similarity.pkl','rb'))

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)