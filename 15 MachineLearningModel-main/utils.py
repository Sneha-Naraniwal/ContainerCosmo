# utils.py
import joblib
from sklearn.preprocessing import LabelEncoder

def train_model(X, y, model_type="Logistic Regression"):
    # Your code for training the model
    pass

def save_model(model, model_type="Logistic Regression"):
    # Your code for saving the model
    pass

def load_model(model_type="Logistic Regression"):
    # Use local imports to avoid circular import issues
    from pages.Upload_Predict import show  # Import only inside this function

    # Load the model and label encoder here
    model_path = f"models/{model_type}_model.pkl"
    model = joblib.load(model_path)
    
    le = joblib.load('models/label_encoder.pkl')  # Load the label encoder

    return model, le  # Return both model and label encoder
