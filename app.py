# app.py
import streamlit as st
from genre_page import genre_recommendations
from mood_page import mood_recommendations
from intro_page import intro_page

def main():
    st.title("Spotify Music Recommendation ")

    menu = ["Intro", "Genre Recommendations", "Mood Recommendations"]
    choice = st.radio("Pilih Halaman", menu)

    if choice == "Intro":
        intro_page()
    elif choice == "Genre Recommendations":
        genre_recommendations()
    elif choice == "Mood Recommendations":
        mood_recommendations()

if __name__ == "__main__":
    main()
