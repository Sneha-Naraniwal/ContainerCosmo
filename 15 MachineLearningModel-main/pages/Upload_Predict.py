import pandas as pd
import streamlit as st
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_model


def show():
    # Ensure that the user has uploaded a dataset
    if 'df' not in st.session_state:
        st.warning("Please upload a dataset first!")
        return
    
    df = st.session_state['df']  # Get the uploaded dataset
    
    # Select the model type for prediction
    model_type = st.selectbox("Select Model Type", ["Logistic Regression", "Random Forest", "SVM", "XGBoost"])
    
    # Load the model and label encoder
    model, le = load_model(model_type)  # Assuming `load_model()` is implemented correctly
    
    # Feature input sliders
    st.subheader("Enter feature values for prediction:")
    
    # Add sliders for input features (adjust slider ranges based on your dataset)
    sepal_length = st.slider("Sepal Length", float(df["sepal_length"].min()), float(df["sepal_length"].max()))
    sepal_width = st.slider("Sepal Width", float(df["sepal_width"].min()), float(df["sepal_width"].max()))
    petal_length = st.slider("Petal Length", float(df["petal_length"].min()), float(df["petal_length"].max()))
    petal_width = st.slider("Petal Width", float(df["petal_width"].min()), float(df["petal_width"].max()))
    
    # Create a DataFrame with the input values for prediction
    input_data = pd.DataFrame({
        "sepal_length": [sepal_length],
        "sepal_width": [sepal_width],
        "petal_length": [petal_length],
        "petal_width": [petal_width]
    })
    
    # Predict using the model
    prediction = model.predict(input_data)
    
    # Decode the predicted label
    predicted_label = le.inverse_transform(prediction)[0]
    st.write(f"Predicted Label: {predicted_label}")
    
    # Accuracy on the uploaded data (current dataset)
    accuracy = calculate_accuracy(df, model, le)
    st.write(f"Model Accuracy on Uploaded Data: {accuracy:.2f}%")
    
    

# Calculate accuracy function for the uploaded data
def calculate_accuracy(df, model, le):
    X = df.drop(columns=["species"])  # Features
    y = df["species"]  # Actual labels
    
    # Encode the target labels using the label encoder
    y_encoded = le.transform(y)
    
    # Predict using the model
    y_pred = model.predict(X)
    
    # Calculate accuracy
    accuracy = accuracy_score(y_encoded, y_pred) * 100
    return accuracy
