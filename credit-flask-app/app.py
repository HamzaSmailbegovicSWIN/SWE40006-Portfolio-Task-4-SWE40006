import os
import socket
from flask import Flask

app = Flask(__name__)

PORT = int(os.environ.get("PORT", 5000))
APP_MESSAGE = os.environ.get("APP_MESSAGE", "Hello from my Dockerised Flask app!")

@app.route("/")
def home():
    return f"""
    <h1>{APP_MESSAGE}</h1>
    <p>Served by container: <b>{socket.gethostname()}</b></p>
    <p>Listening on port: <b>{PORT}</b></p>
    """

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)