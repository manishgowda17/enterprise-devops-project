from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 Enterprise DevOps Platform</h1>
    <h2>Production CI/CD Pipeline</h2>
    <ul>
        <li>✅ Jenkins CI/CD</li>
        <li>✅ Docker</li>
        <li>✅ Docker Compose</li>
        <li>✅ AI Deployment Analyzer</li>
        <li>✅ Health Checks</li>
        <li>✅ Project Validation</li>
        <li>✅ Running on AWS EC2</li>
    </ul>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000))
