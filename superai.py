import streamlit as st
import openai
from datetime import datetime
import random

# Set up the app
st.set_page_config(page_title="VibinAI", layout="wide")

# Header Section
st.title("🎵 VibinAI - Personalized Mood Playlists 🎶")
st.subheader("Your AI companion for music and mindfulness")

# Sidebar for user input
st.sidebar.title("Set Your Vibe 🌈")
mood = st.sidebar.text_input("Describe your mood in one sentence:")
weather = st.sidebar.selectbox("What's the weather like?", ["Sunny", "Rainy", "Cloudy", "Snowy", "Windy"])
heart_rate = st.sidebar.slider("Heart Rate (BPM)", min_value=50, max_value=150, value=75)
generate_btn = st.sidebar.button("Generate Playlist 🎧")

# Main App Logic
if generate_btn:
    # Placeholder for AI-generated playlist
    playlist = [
        f"Track {i+1} - {random.choice(['Happy', 'Chill', 'Focus', 'Energetic', 'Relax'])} Vibes"
        for i in range(5)
    ]
    
    # Personalized message
    mood_summary = f"You're feeling {'calm' if heart_rate < 80 else 'active'}. The weather is {weather.lower()}."
    st.success(f"✨ {mood_summary}")
    
    # Display Playlist
    st.header("🎼 Your Personalized Playlist")
    for track in playlist:
        st.write(f"- {track}")
    
    # Well-being tips
    st.header("🌿 Well-being Insights")
    if heart_rate < 80:
        st.info("Take this time to relax and enjoy the moment!")
    else:
        st.info("Feeling energetic? Try a quick workout or dance session!")
    
    st.markdown("---")
    
    # Social Sharing Button
    st.markdown("🚀 **Share Your Vibe!** [Click here to share](#)")

# Footer
st.markdown("© 2024 VibinAI | Crafted with ❤️ and Streamlit")
streamlit run superai.py
