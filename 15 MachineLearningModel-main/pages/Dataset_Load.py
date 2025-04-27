import streamlit as st
import pandas as pd

def show():
    st.title("📂 Dataset Load")
    
    file = st.file_uploader("Upload a CSV file", type="csv")
    if file is not None:
        df = pd.read_csv(file)
        st.write("Dataset Preview:")
        st.dataframe(df.head())
        st.session_state['df'] = df  # Store dataset in session state
    else:
        st.warning("Please upload a dataset.")
