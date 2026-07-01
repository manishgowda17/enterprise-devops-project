from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Enterprise DevOps Platform</h1><p>Welcome to Day 2 Project!</p>"

@app.route("/health")
def health():
    return {"status": "Healthy"}

@app.route("/version")
def version():
    return {"version": "1.0.0"}

@app.route("/hostname")
def hostname():
    return {"hostname": socket.gethostname()}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
