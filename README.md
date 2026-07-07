Day 1 – Setup
Created project structure for DevOps tools (Docker, Kubernetes, Terraform, Jenkins)
Initialized Git repository and pushed to GitHub
Added .gitignore and organized folders


Day 2 – Docker + Flask App
Built Flask web app with /, /health, /version, /hostname endpoints
Used Gunicorn for production server
Created production-ready Dockerfile (security + optimized layers)
Built and ran Docker container on EC2
Exposed app on port 5000 and tested endpoints
Learned Docker basics: image, container, port mapping


Day 3 – Multi-Container Application with Docker Compose

- Created a multi-container architecture using Docker Compose.
- Integrated Flask application, PostgreSQL, and Redis.
- Configured custom Docker bridge network for container communication.
- Added persistent storage using Docker volumes.
- Managed application configuration with environment variables.
- Implemented automatic restart policies.
- Learned service dependencies and container orchestration using Docker Compose.
- 

##  Day 4: Jenkins CI/CD Pipeline with AI Build Summary

### Project Overview

This project demonstrates an end-to-end CI/CD pipeline built using Jenkins, Docker, Docker Compose, Python, and AWS EC2. The pipeline automates application deployment while incorporating an AI-powered build summary to showcase the integration of AI into DevOps workflows.

---

## Technologies Used

* Git & GitHub
* Jenkins
* Docker
* Docker Compose
* Python
* AWS EC2 (Ubuntu)
* Linux

---

## Pipeline Workflow

1. Checkout the latest source code from GitHub.
2. Verify Docker and Docker Compose installation.
3. Build the Docker image.
4. Deploy the application using Docker Compose.
5. Execute the AI Build Summary script.
6. Perform a health check on the deployed application.
7. Clean up unused Docker images.

---

## AI Build Summary

A lightweight Python script (`scripts/aibuild.py`) is executed during the pipeline to generate an automated build summary. This demonstrates how AI concepts can be integrated into CI/CD pipelines to improve deployment visibility and automate reporting.

---

## Features

* Automated CI/CD using Jenkins
* Docker image creation
* Docker Compose deployment
* AI-powered build summary
* Automated health check
* Automatic Docker image cleanup
* Deployment on AWS EC2

---

## Key Learning Outcomes

* Jenkins Declarative Pipelines
* Docker-based application deployment
* CI/CD automation
* GitHub integration with Jenkins
* AI integration into DevOps workflows
* Troubleshooting real-world deployment issues

Day 5

Project validation (scripts/validate.sh)
Enhanced health check with Docker logs on failure
Pipeline summary
AI deployment report generation
Artifact archiving
Smart Docker cleanup (image prune and builder prune)
Production-style Jenkins pipeline
Final testing and successful deployment
