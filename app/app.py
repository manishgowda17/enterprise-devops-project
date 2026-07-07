from flask import Flask, jsonify
import os
from datetime import datetime

app = Flask(__name__)

BUILD_NUMBER = os.getenv("BUILD_NUMBER", "Local Build")
ENVIRONMENT = os.getenv("ENVIRONMENT", "Production")


@app.route("/")
def home():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Enterprise DevOps Platform</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f6f9;
                margin: 0;
                padding: 40px;
            }}

            .container {{
                max-width: 900px;
                margin: auto;
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,.2);
            }}

            h1 {{
                color: #2c3e50;
            }}

            h2 {{
                color: #27ae60;
            }}

            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }}

            table, th, td {{
                border: 1px solid #ddd;
            }}

            th, td {{
                padding: 12px;
                text-align: left;
            }}

            th {{
                background: #2c3e50;
                color: white;
            }}

            .success {{
                color: green;
                font-weight: bold;
            }}
        </style>
    </head>

    <body>

    <div class="container">

        <h1>🚀 Enterprise DevOps Platform</h1>

        <h2>Production CI/CD Dashboard</h2>

        <table>

            <tr>
                <th>Feature</th>
                <th>Status</th>
            </tr>

            <tr>
                <td>Jenkins CI/CD</td>
                <td class="success">✅ Enabled</td>
            </tr>

            <tr>
                <td>Docker</td>
                <td class="success">✅ Running</td>
            </tr>

            <tr>
                <td>Docker Compose</td>
                <td class="success">✅ Running</td>
            </tr>

            <tr>
                <td>AI Build Analyzer</td>
                <td class="success">✅ Enabled</td>
            </tr>

            <tr>
                <td>DevSecOps Security Scan</td>
                <td class="success">✅ Enabled</td>
            </tr>

            <tr>
                <td>Health Monitoring</td>
                <td class="success">✅ Healthy</td>
            </tr>

            <tr>
                <td>AWS EC2 Deployment</td>
                <td class="success">✅ Live</td>
            </tr>

        </table>

        <br>

        <h3>Build Information</h3>

        <ul>
            <li><strong>Environment:</strong> {ENVIRONMENT}</li>
            <li><strong>Build Number:</strong> {BUILD_NUMBER}</li>
            <li><strong>Deployment Time:</strong> {datetime.now()}</li>
        </ul>

    </div>

    </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "Enterprise DevOps Platform"
    })


@app.route("/version")
def version():
    return jsonify({
        "application": "Enterprise DevOps Platform",
        "version": "1.0",
        "environment": ENVIRONMENT,
        "build_number": BUILD_NUMBER
    })


@app.route("/metrics")
def metrics():
    return jsonify({
        "uptime": "Running",
        "docker": "Healthy",
        "jenkins": "Connected",
        "deployment": "Successful"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
