
  
# Enterprise CI/CD DevOps Platform

An end-to-end Enterprise DevOps Project demonstrating a complete CI/CD pipeline using **Jenkins**, **Docker**, **Docker Compose**, **Nginx**, **PostgreSQL**, **Redis**, and **AWS EC2**.

The application itself is intentionally simple—the primary objective of this project is to showcase an automated DevOps workflow from source code to production deployment.

---

## Project Overview

This project demonstrates how modern DevOps practices automate software delivery.

Whenever code is pushed to GitHub, Jenkins automatically:

- Retrieves the latest source code
- Builds the Docker image
- Performs security and deployment checks
- Deploys the application using Docker Compose
- Starts all required services
- Runs health verification
- Makes the application available on AWS EC2

---

# Architecture

```
                 GitHub Repository
                        │
                        ▼
                 Jenkins Pipeline
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
 Docker Build     Security Scan     AI Analyzer
        │
        ▼
 Docker Compose Deployment
        │
 ┌──────┴─────────────┐
 ▼                    ▼
Flask App          Nginx
 │
 ├──────────────┐
 ▼              ▼
PostgreSQL    Redis
        │
        ▼
AWS EC2 Production Server
```

---

# Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Framework | Flask |
| CI/CD | Jenkins |
| Containerization | Docker |
| Orchestration | Docker Compose |
| Reverse Proxy | Nginx |
| Database | PostgreSQL |
| Cache | Redis |
| Cloud | AWS EC2 |
| Version Control | Git & GitHub |
| Web Server | Gunicorn |

---

# Project Structure

```
enterprise-devops-project/

├── app/
│   ├── app.py
│   ├── models.py
│   ├── requirements.txt
│   └── ...
│
├── docker/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── nginx.conf
│
├── Jenkinsfile
│
├── README.md
│
└── screenshots/
```

---

#  CI/CD Pipeline

The Jenkins pipeline performs the following stages:

### 1️. Source Code Checkout

- Fetches latest code from GitHub

---

### 2️. Build Docker Image

- Creates Docker image
- Tags image
- Validates build

---

### 3️. Deploy Application

Uses Docker Compose to deploy:

- Flask Application
- PostgreSQL
- Redis
- Nginx

---

### 4️. AI Deployment Analyzer

Performs deployment validation.

---

### 5. DevSecOps Security Scan

Checks the deployment for common security issues.

---

### 6️. Health Check

Verifies:

- Application availability
- Running containers
- Deployment success

---

### 7. Pipeline Summary

Archives reports and completes deployment.

---

# Docker Services

The application consists of four containers:

| Container | Purpose |
|-----------|----------|
| Flask | Web Application |
| PostgreSQL | Database |
| Redis | Cache |
| Nginx | Reverse Proxy |

---

# Application Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Home Page |
| `/health` | Health Status |
| `/version` | Version Information |
| `/metrics` | Deployment Metrics |
| `/deployment` | Latest Deployment |
| `/db-status` | PostgreSQL Status |
| `/redis-status` | Redis Status |

---

# Deployment Workflow

```
Developer

     │

     ▼

GitHub Push

     │

     ▼

Jenkins Pipeline

     │

     ▼

Docker Image Build

     │

     ▼

Docker Compose Deployment

     │

     ▼

Nginx Reverse Proxy

     │

     ▼

Flask Application

     │

 ┌───┴────┐

 ▼        ▼

PostgreSQL   Redis

     │

     ▼

AWS EC2
```

---

#  Project Screenshots

#RUNNING PROJECT VALIDATION


<img width="1920" height="918" alt="running project validation" src="https://github.com/user-attachments/assets/2b9d6b0c-7263-48eb-8986-4c535c6328da" />


#AI DEPLOYMENT ANALYZER


<img width="1920" height="918" alt="ai deployment analyzer" src="https://github.com/user-attachments/assets/78777ff1-49a7-4834-9fe8-104082dba738" />


#AI SECURITY ANALYSIS


<img width="1920" height="918" alt="ai security analysis" src="https://github.com/user-attachments/assets/df268a11-4624-4f61-ae1c-f2142e478721" />


#DEVSECOPS SECURITY SCAN


<img width="1920" height="918" alt="devsecops security scan" src="https://github.com/user-attachments/assets/aad726af-2a3d-4cfe-8e9b-c447270717e5" />


#APPLICATION HEALTH


<img width="1920" height="918" alt="application health" src="https://github.com/user-attachments/assets/4fad7d70-d0f0-43eb-bf84-5b1804282d81" />


#PIPELINE SUMMARY


<img width="1920" height="918" alt="pipeline summary" src="https://github.com/user-attachments/assets/84d8ffe8-9989-4205-9957-67438348da90" />


#AI DEPLOYMENT REPORT


<img width="1920" height="918" alt="ai deployment report" src="https://github.com/user-attachments/assets/6d4bb2cf-62d1-4949-9d98-706695929c26" />


#JENKINS PIPELINE SUCCESS


<img width="1920" height="918" alt="jenkins pipeline success" src="https://github.com/user-attachments/assets/4f8f05c3-5259-4133-8c84-30faa2ee61e5" />


#DASHBOARD


<img width="1920" height="918" alt="ss" src="https://github.com/user-attachments/assets/ebd0b8f2-e800-441c-942c-4e430f7ca7b8" />




---

# Running the Project

Clone the repository

```bash
git clone https://github.com/manishgowda17/enterprise-devops-project.git
```

Go to project directory

```bash
cd enterprise-devops-project
```

Build Docker image

```bash
docker build -f docker/Dockerfile -t enterprise-devops .
```

Run using Docker Compose

```bash
docker compose -f docker/docker-compose.yml up -d
```

Access application


```
http://<EC2-Public-IP>
```

---

#  Features

- Automated CI/CD Pipeline
- Dockerized Application
- Multi-container Deployment
- Reverse Proxy with Nginx
- PostgreSQL Integration
- Redis Integration
- AWS EC2 Deployment
- Health Monitoring
- AI Deployment Analysis
- DevSecOps Security Scan

---

#  Learning Outcomes

Through this project, I gained practical experience with:

- CI/CD Automation
- Docker & Docker Compose
- Jenkins Pipelines
- Reverse Proxy Configuration
- PostgreSQL Integration
- Redis Integration
- AWS EC2 Deployment
- Production Deployment Workflow
- Health Monitoring
- Enterprise DevOps Practices

---

LinkedIn: www.linkedin.com/in/
manish-gowda-s-n-a75a19332



