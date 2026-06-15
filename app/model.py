# app/model.py

import joblib
import os

# take path of file model.py
current_dir = os.path.dirname(os.path.abspath(__file__))
# take root folder of app (Prject spam ham)
base_dir = os.path.dirname(current_dir)

# Create accurate path to fil .pkl
model_path = os.path.join(base_dir, 'model', 'model.pkl')
vectorizer_path = os.path.join(base_dir, 'model', 'vectorizer.pkl')

# Load trained model + vectorizer
model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

def predict_email(text: str):
    # 1. Convert text to vector (sparse matrix)
    X = vectorizer.transform([text])
    
    # 2. Conver to  DENSE MATRIX (key)
    X_dense = X.toarray()
    
    # 3. Predict on X_dense instead of X
    pred = model.predict(X_dense)[0]
    
    return "spam" if pred == 1 else "ham"