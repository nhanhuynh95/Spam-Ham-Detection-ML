
===============================================================================================
Local Development:
At terminal:
pip install fastapi uvicorn pandas matplotlib seaborn nltk scikit-learn pydantic joblib numpy
python -m uvicorn app.main:app --reload

Then access the service:
API Interface: http://127.0.0.1:8000/docs
Web UI: http://127.0.0.1:8000/ui

To view the database logs, use the "SQLite Viewer" extension in VS Code to open spam_logs.db
===============================================================================================
Docker Deployment

docker build -t spam-detection-app .
docker run -d -p 8000:8000 spam-detection-app

To see the frontend application:
https://spam-ham-detection-ml.onrender.com/ui

