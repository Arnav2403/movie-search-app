import streamlit as st
import pandas as pd
import requests
import re

API_KEY = '5db739c4'
BASE_URL = 'http://www.omdbapi.com/'

def clean_title(title):
    return re.sub("[^a-zA-Z0-9 ]", "", str(title)).lower()

def search_movies(query):
    params = {'apikey': API_KEY, 's': query}
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        if "Search" in data:
            movies = pd.DataFrame(data['Search'])
            movies.dropna(subset=["Title", "Year"], inplace=True)
            
            def get_movie_details(imdb_id):
                details_params = {'apikey': API_KEY, 'i': imdb_id}
                details_response = requests.get(BASE_URL, params=details_params)
                details_data = details_response.json()
                return (
                    details_data.get('Genre', 'N/A'),
                    details_data.get('Poster', 'https://via.placeholder.com/200x300?text=No+Image'),
                    details_data.get('imdbRating', 'N/A'),
                    details_data.get('Actors', 'N/A'),
                    details_data.get('Director', 'N/A'),
                    details_data.get('Plot', 'N/A')
                )
            
            movies[["Genre", "Poster", "IMDB Rating", "Cast", "Director", "Plot"]] = movies['imdbID'].apply(lambda imdb_id: pd.Series(get_movie_details(imdb_id)))
            movies["clean_title"] = movies["Title"].apply(clean_title)
            return movies
        else:
            return pd.DataFrame()
    except requests.exceptions.RequestException as e:
        st.error(f"API request failed: {e}")
        return pd.DataFrame()

st.title("🎬 Movie Search App")
movie_query = st.text_input("Enter movie title:", "Inception")

if st.button("Search"):
    st.write("🔍 Searching for movies...")
    results = search_movies(movie_query)
    if not results.empty:
        for _, row in results.head(10).iterrows():
            with st.container():
                st.markdown(f"## {row['Title']} ({row['Year']})")
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.image(row['Poster'], width=200)
                with col2:
                    st.write(f"**🎭 Genre:** {row['Genre']}")
                    st.write(f"**⭐ IMDB Rating:** {row['IMDB Rating']} ⭐")
                    st.write(f"**🎬 Director:** {row['Director']}")
                    st.write(f"**👥 Cast:** {row['Cast']}")
                    st.write(f"**📖 Plot:** {row['Plot']}")
    else:
        st.warning("❌ Movie not found! Try another title.")

