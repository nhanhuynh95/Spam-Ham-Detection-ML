# app/model.py

import joblib
import os

<<<<<<< HEAD
# take path of file model.py
current_dir = os.path.dirname(os.path.abspath(__file__))
# take root folder of app (Prject spam ham)
base_dir = os.path.dirname(current_dir)

# Tạo đường dẫn chính xác tới file .pkl
# Create accurate path to fil .pkl
=======
# Lấy đường dẫn của file model.py này
current_dir = os.path.dirname(os.path.abspath(__file__))
# Lấy thư mục cha của app (chính là thư mục project Spam ham)
base_dir = os.path.dirname(current_dir)

# Tạo đường dẫn chính xác tới file .pkl
>>>>>>> origin/main
model_path = os.path.join(base_dir, 'model', 'model.pkl')
vectorizer_path = os.path.join(base_dir, 'model', 'vectorizer.pkl')

# Load trained model + vectorizer
model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

def predict_email(text: str):
<<<<<<< HEAD
    # 1. Convert text to vector (sparse matrix)
    X = vectorizer.transform([text])
    
    # 2. Conver to  DENSE MATRIX (key)
    X_dense = X.toarray()
    
    # 3. Predict on X_dense instead of X
=======
    # 1. Biến text thành vector (vẫn là sparse matrix)
    X = vectorizer.transform([text])
    
    # 2. CHUYỂN THÀNH DENSE MATRIX (Đây là chìa khóa!)
    X_dense = X.toarray()
    
    # 3. Predict trên X_dense thay vì X
>>>>>>> origin/main
    pred = model.predict(X_dense)[0]
    
    return "spam" if pred == 1 else "ham"