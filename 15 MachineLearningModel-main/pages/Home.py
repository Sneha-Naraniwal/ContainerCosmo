# pages/Home.py
import streamlit as st

def show():
    st.title("🏠 Welcome to the Machine Learning App")
    st.write("Use the sidebar to navigate through the different steps:")
    st.markdown("""
    - Load a dataset
    - Train a Machine Learning model
    - Upload new data for predictions
    - Visualize model performance
    -Analyze the data drift
    """)
