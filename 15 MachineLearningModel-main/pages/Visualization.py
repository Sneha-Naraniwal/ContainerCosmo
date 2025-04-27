import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ks_2samp  # Kolmogorov-Smirnov Test for numerical features

# Function to calculate and display data drift using Kolmogorov-Smirnov Test for numerical features
def detect_drift(current_data, historical_data, feature_columns):
    drift_results = {}
    
    for feature in feature_columns:
        # Perform KS test on the feature (Numerical feature drift detection)
        ks_stat, p_value = ks_2samp(current_data[feature], historical_data[feature])
        
        # Store the result
        drift_results[feature] = {
            "KS Statistic": ks_stat,
            "p-value": p_value
        }
    
    return drift_results

def show():
    # Load the current dataset (ensure it's in session state)
    if 'df' not in st.session_state:
        st.warning("Please upload or load a dataset first!")
        return
    
    df = st.session_state['df']
    
    # Use the current data as historical data temporarily
    historical_data = df.copy()  # This will simulate historical data as a copy of the current dataset
    
    # Radio button to select drift detection type
    drift_detection_option = st.radio("Select Data Drift Detection Method", ["None", "Drift Detection"])

    if drift_detection_option == "Drift Detection":
        # Feature columns to check for drift (you can modify this based on your dataset)
        feature_columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']  # Example for Iris dataset
        
        # Run data drift detection
        drift_results = detect_drift(df, historical_data, feature_columns)
        
        # Display Drift Results
        st.write("Data Drift Detection Results:")
        drift_df = pd.DataFrame(drift_results).T
        drift_df['Drift Detected'] = drift_df['p-value'] < 0.05  # If p-value < 0.05, drift detected
        st.write(drift_df)
        
        # Optional: Visualize data drift with histograms
        st.subheader("Visualize Data Drift for Selected Features")
        
        for feature in feature_columns:
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.histplot(df[feature], color="blue", kde=True, label="Current Data", ax=ax)
            sns.histplot(historical_data[feature], color="red", kde=True, label="Historical Data", ax=ax)
            ax.set_title(f"Distribution Comparison for {feature}")
            ax.legend()
            st.pyplot(fig)
