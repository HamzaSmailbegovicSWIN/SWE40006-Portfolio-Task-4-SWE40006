import os
import socket
from datetime import datetime, timezone
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

APP_NAME = os.getenv("APP_NAME", "Distinction Web App")
APP_ENV = os.getenv("APP_ENV", "development")
APP_VERSION = os.getenv("APP_VERSION", "1.0")
STUDENT_NAME = os.getenv("STUDENT_NAME", "Student")

app = FastAPI(title=APP_NAME)

@app.get("/", response_class=HTMLResponse)
def home():
    return f"""
    <html>
      <head><title>{APP_NAME}</title></head>
      <body style="font-family: sans-serif; max-width: 700px; margin: 40px auto;">
        <h1>{APP_NAME}</h1>
        <p>Deployed by: <b>{STUDENT_NAME}</b></p>
        <p>Environment: <b>{APP_ENV}</b> | Version: <b>{APP_VERSION}</b></p>
        <p>Served by container: <b>{socket.gethostname()}</b></p>
        <p>Endpoints: <a href="/health">/health</a> | <a href="/info">/info</a> | <a href="/docs">/docs</a></p>
      </body>
    </html>
    """

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/info")
def info():
    return {
        "app_name": APP_NAME,
        "environment": APP_ENV,
        "version": APP_VERSION,
        "student": STUDENT_NAME,
        "container_hostname": socket.gethostname(),
        "server_time_utc": datetime.now(timezone.utc).isoformat(),
    }