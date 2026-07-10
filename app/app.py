from flask import Flask, jsonify
from models import db, Employee
import os
from datetime import datetime

app = Flask(__name__)

DB_HOST = os.getenv("DATABASE_HOST", "postgres")
DB_PORT = os.getenv("DATABASE_PORT", "5432")
DB_NAME = os.getenv("DATABASE_NAME", "enterprise_db")
DB_USER = os.getenv("DATABASE_USER", "admin")
DB_PASSWORD = os.getenv("DATABASE_PASSWORD", "admin123")

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

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
@app.route("/employees")
def employees():

    employee_list = Employee.query.all()

    data = []

    for emp in employee_list:
        data.append({
            "id": emp.id,
            "name": emp.name,
            "email": emp.email,
            "role": emp.role,
            "department": emp.department
        })

    return jsonify(data)
with app.app_context():
    db.create_all()

    if Employee.query.count() == 0:
        sample_employees = [
            Employee(
                name="Manish Gowda",
                email="manish@enterprise.com",
                role="DevOps Engineer",
                department="Platform"
            ),
            Employee(
                name="mishh",
                email="mishh@enterprise.com",
                role="Cloud Engineer",
                department="Cloud"
            ),
            Employee(
                name="man",
                email="man@enterprise.com",
                role="Site Reliability Engineer",
                department="Operations"
            )
        ]

        db.session.add_all(sample_employees)
        db.session.commit()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
