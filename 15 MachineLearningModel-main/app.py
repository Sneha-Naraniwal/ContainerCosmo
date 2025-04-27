import streamlit as st
from pages import Home, Dataset_Load, Train_Models, Upload_Predict, Visualization

st.set_page_config(page_title="ML Training and Predictions", layout="wide")

# Navigation Sidebar
st.sidebar.title("Machine Learning App")
option = st.sidebar.radio("Select Page", ["Home", "Dataset", "Train Model", "Make Predictions", "Visualization"])

if option == "Home":
    Home.show()
elif option == "Dataset":
    Dataset_Load.show()
elif option == "Train Model":
    Train_Models.show()
elif option == "Make Predictions":
    Upload_Predict.show()
else:
    Visualization.show()
