# app/main.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.schema import EmailRequest, PredictionResponse
from app.model import predict_email
import os 
import sqlite3 #r3 for database
from datetime import datetime #r3 for database

app = FastAPI(
    title="Spam Detection API",
    description="End-to-end ML system for email spam classification",
    version="1.0"
)

# =======================================================
# r3: Database Initialization (run when turn on server)
# =======================================================
def init_db():
    conn = sqlite3.connect("spam_logs.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT,
            label TEXT,
            timestamp DATETIME
        )
    """)
    conn.commit()
    conn.close()
# Call initial function when load file main.py
init_db()
# =======================================================

# current API
@app.get("/")
def home():
    return {"message": "Spam Detection API is running"}

@app.post("/predict", response_model=PredictionResponse)
def predict(request: EmailRequest):
    label = predict_email(request.text)
    
    # =======================================================
    # r3: save log in to DATABASE
    # =======================================================
    conn = sqlite3.connect("spam_logs.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO predictions (text, label, timestamp) VALUES (?, ?, ?)",
        (request.text, label, datetime.now())
    )
    conn.commit()
    conn.close()
    # =======================================================
    
    return PredictionResponse(label=label)


# r2-frontend
@app.get("/ui", response_class=HTMLResponse)
async def get_ui():
        # take folder path contain file main.py is 'app'
    base_dir = os.path.dirname(os.path.abspath(__file__))
        # go back 1 layer out off app then go into templates
    file_path = os.path.join(os.path.dirname(base_dir), "templates", "index.html")
    
    with open(file_path, "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())
    
# r4-homepage
@app.get("/", response_class=HTMLResponse)
async def home_page():
    return await get_ui()
# -----------------------------------
    
    
