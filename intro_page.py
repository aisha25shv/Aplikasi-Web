# intro_page.py
import streamlit as st
from PIL import Image

def intro_page():

    # Tambahkan teks intro dengan pewarnaan dan format yang menarik
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');

        body {
            font-family: 'Poppins', sans-serif;
            background-color: #f0f0f0;
            color: #333333;
        }

        h1 {
            font-family: 'Poppins', sans-serif;
            text-align: center;
        }

        p {
            font-family: 'Poppins', sans-serif;
        }
        </style>
        """
        , unsafe_allow_html=True
    )

    st.write(
        "Selamat datang di **Sistem Rekomendasi Musik!** 🎵\n\n"
        "Sistem ini membantu Anda menemukan lagu-lagu berdasarkan genre dan mood.\n"
        "Pilih salah satu dari dua opsi di sidebar untuk melihat rekomendasi lagu."
    )

    st.write(
        "- **Genre Recommendations**: Temukan lagu-lagu berdasarkan genre musik favorit Anda.\n"
        "- **Mood Recommendations**: Dapatkan rekomendasi lagu berdasarkan suasana hati yang sedang Anda rasakan."
    )

    st.write(
        "**Nikmati pengalaman menemukan musik baru!** 🎶\n\n"
        "_Explore the world of music with us!_ 🌈"
    )
