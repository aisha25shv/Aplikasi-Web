# genre_page.py
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def genre_recommendations():
    st.subheader("Genre Recommendations")
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');

        body {
            font-family: 'Poppins', sans-serif;
        }
        
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Poppins', sans-serif;
            text-align: center;  /* Teks menjadi pusat */
        }
        
        /* Your existing styles go here */

        </style>
        """, unsafe_allow_html=True
    )

    # Load data and perform necessary operations
    artists_total = pd.read_csv('artists_total.csv')
    audio_mood = pd.read_csv('audio_mood.csv')
    merged_data = pd.merge(artists_total, audio_mood, how='inner', on='artist')
    features = merged_data[['genres', 'mood', 'track', 'artist']]

    # Clean up genre format
    features['genres'] = features['genres'].apply(lambda x: ', '.join([genre.strip("[]'\"") for genre in x.split(',')]))
    features['genres'] = features['genres'].apply(lambda x: x.replace('"', '').strip())

    # Ensure all values in 'genres' column are strings
    features['genres'] = features['genres'].astype(str)

    # Extract features
    vectorizer = CountVectorizer()
    features_matrix = vectorizer.fit_transform(features['genres'] + ',' + features['mood'])
    similarity_matrix = cosine_similarity(features_matrix, features_matrix)

    # Get all genres
    all_genres = sorted(set([genre.strip("[]'\" ") for sublist in features['genres'].explode() for genre in sublist.split(',')]))

    # Remove double quotes from each genre in the dropdown
    all_genres_cleaned = [genre.replace('"', '') for genre in all_genres]

    # Dropdown for genre selection
    selected_genre = st.selectbox('Select Genre', all_genres_cleaned)

    # Function to display recommendations based on genre
    display_genre_recommendations(features, selected_genre)

# Function to display recommendations based on genre
def display_genre_recommendations(features, selected_genre):
    # Filter dataset based on selected genre
    filtered_data = features[features['genres'].apply(lambda x: selected_genre in x)]

    # Check if filtered_data is empty
    if len(filtered_data) == 0:
        st.warning(f"No songs with the selected genre '{selected_genre}'.")
        return

    # Get one song from each artist randomly
    recommended_songs_info = filtered_data.groupby('artist').apply(lambda group: group.sample(1)).reset_index(drop=True)

    # Display DataFrame with title, artist, mood, and genres
    st.table(recommended_songs_info[['track', 'artist', 'mood', 'genres']].apply(lambda x: x.astype(str).str.replace('[','').str.replace(']','').str.replace("'",'').str.strip(), axis=1))
