import streamlit as st
import shap
import pandas as pd
from utils import train_model, save_model
import xgboost as xgb  # For XGBoost model

def show():
    st.title("🎯 Train a Model")

    if 'df' not in st.session_state:
        st.warning("Please upload or load a dataset first!")
        return

    df = st.session_state['df']
    target = st.selectbox("Select Target Variable", df.columns)

    features = st.multiselect("Select Feature Variables", [col for col in df.columns if col != target])

    model_type = st.selectbox("Choose Model Type", ["Logistic Regression", "Random Forest", "SVM", "XGBoost"])

    if st.button("Train Model"):
        X = df[features]
        y = df[target]

        model = train_model(X, y, model_type=model_type)

        # SHAP values calculation for tree-based models (XGBoost, Random Forest)
        if model_type in ["XGBoost", "Random Forest"]:
            explainer = shap.TreeExplainer(model)
            shap_values = explainer.shap_values(X)

            # Visualize SHAP values
            st.write("SHAP values visualization")
            shap.summary_plot(shap_values, X)
            st.pyplot()  # This will render the plot

        save_model(model, model_type)
        st.success(f"Model {model_type} trained and saved successfully!")
