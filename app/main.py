from fastapi import FastAPI
from threading import Thread
from app.log_watcher import start_watcher
from app.log_analyzer import analyze_logs

app = FastAPI()

# Start real-time log watcher on startup
@app.on_event("startup")
def startup_event():
    Thread(target=start_watcher, daemon=True).start()

@app.get("/")
def home():
    return {"message": "AI SOC running with real-time log monitoring and AI anomaly detection 🚀"}

@app.get("/analyze")
def analyze():
    """
    Analyze the log file for suspicious and anomalous activity.
    Returns a list of threats detected by static checks and AI.
    """
    LOG_FILE = "sample.log"
    threats = analyze_logs(LOG_FILE)
    return {"threats": threats}