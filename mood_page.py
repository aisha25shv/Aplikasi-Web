# mood_page.py
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def mood_recommendations():
    st.subheader("Mood Recommendations")
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

    # Get all moods
    all_moods = sorted(features['mood'].unique())

    # Dropdown for mood selection
    selected_mood = st.selectbox('Select Mood', all_moods)

    # Function to display recommendations based on mood
    display_mood_recommendations(features, selected_mood)

# Function to display recommendations based on mood
def display_mood_recommendations(features, selected_mood):
    # Filter dataset based on selected mood
    filtered_data = features[features['mood'] == selected_mood]

    # Check if filtered_data is empty
    if len(filtered_data) == 0:
        st.warning(f"No songs with the selected mood '{selected_mood}'.")
        return

    # Get one song from each artist randomly
    recommended_songs_info = filtered_data.groupby('artist').apply(lambda group: group.sample(1)).reset_index(drop=True)

    # Display DataFrame with title, artist, mood, and genres
    st.table(recommended_songs_info[['track', 'artist', 'mood', 'genres']].apply(lambda x: x.astype(str).str.replace('[','').str.replace(']','').str.replace("'",'').str.strip(), axis=1))
