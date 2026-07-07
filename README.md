# 🚀 Enterprise DevOps Platform










# 📖 Project Overview

Enterprise DevOps Platform is a complete end-to-end DevOps project that demonstrates how a modern application can be built, containerized, validated, secured, deployed, and monitored using industry-standard DevOps tools.

The project was developed as a hands-on learning experience by implementing a real Continuous Integration and Continuous Deployment (CI/CD) pipeline on an AWS EC2 instance using Jenkins, Docker, Docker Compose, Linux, Git, and Python.

Instead of focusing only on deployment, this project also integrates lightweight DevSecOps practices such as security validation, project validation, AI-assisted build reporting, health monitoring, and deployment reporting.

The objective was to simulate a production-style DevOps workflow while keeping the infrastructure lightweight enough to run on a free-tier AWS EC2 instance.
# 🎯 Project Objectives

The primary objectives of this project are:

- Automate software build and deployment using Jenkins
- Containerize applications using Docker
- Deploy applications using Docker Compose
- Integrate DevSecOps practices into CI/CD
- Perform project validation before deployment
- Generate AI-assisted deployment summaries
- Monitor application health
- Archive deployment and security reports
- Demonstrate a production-style DevOps workflow

---

# ✨ Key Features

## 🔄 Continuous Integration (CI)

- Automated source code checkout from GitHub
- Jenkins Declarative Pipeline
- Docker image build automation
- Build verification
- Automated deployment process

---

## 🚀 Continuous Deployment (CD)

- Docker Compose deployment
- Automatic container recreation
- One-click deployment using Jenkins
- Health verification after deployment

---

## 🔒 DevSecOps Features

- Secret detection
- Project validation
- Docker configuration validation
- Dependency validation
- Security report generation

---

## 🤖 AI Build Analyzer

A custom Python script generates deployment summaries containing:

- Build Number
- Job Name
- Workspace Information
- Deployment Status
- Security Summary
- Build Report

---

## ❤️ Health Monitoring

The application exposes monitoring endpoints:

| Endpoint | Description |
|----------|-------------|
| `/` | Enterprise Dashboard |
| `/health` | Application Health Status |
| `/version` | Application Version |
| `/metrics` | Basic Application Metrics |

---

## ☁ Cloud Deployment

The application is deployed on:

- AWS EC2 (Ubuntu)
- Docker Engine
- Docker Compose
- Jenkins

---

# 🛠 Technology Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python 3 |
| Web Framework | Flask |
| Version Control | Git |
| Repository Hosting | GitHub |
| CI/CD | Jenkins |
| Containerization | Docker |
| Container Orchestration | Docker Compose |
| Cloud Platform | AWS EC2 |
| Operating System | Ubuntu Linux |
| Scripting | Bash |
| DevSecOps | Custom Security Scanner |
| Monitoring | Health Endpoints |
| Reporting | AI Build Analyzer |

---

# 🏗 Project Architecture

```text
                        GitHub Repository
                               │
                               ▼
                        Jenkins Pipeline
                               │
         ┌─────────────────────┼─────────────────────┐
         ▼                     ▼                     ▼
 Project Validation     Security Scan       AI Build Analysis
         │
         ▼
 Docker Image Build
         │
         ▼
 Docker Compose Deployment
         │
         ▼
 Flask Web Application
         │
         ▼
 Health Monitoring
         │
         ▼
 Deployment & Security Reports
```

---

# 📂 Project Structure

```text
enterprise-devops-project/
│
├── app/
│   ├── app.py
│   └── requirements.txt
│
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── jenkins/
│   └── Jenkinsfile
│
├── scripts/
│   ├── validate.sh
│   ├── security_scan.sh
│   └── aibuild.py
│
├── reports/
│   ├── deployment_report.txt
│   └── security_report.txt
│
├── screenshots/
│
├── README.md
│
└── .gitignore
```

---

# 📸 Project Screenshots

AI ANALYSIS


<img width="1920" height="918" alt="jen ai analysis" src="https://github.com/user-attachments/assets/64a83b42-9d22-4608-9200-d18ae5559e72" />


AI ANALYZER


<img width="1920" height="918" alt="jen ai analyzer" src="https://github.com/user-attachments/assets/45761610-0ee4-4dfd-beb7-bad069701631" />


JENKINS DASHBOARD


<img width="1920" height="918" alt="jen dashboard" src="https://github.com/user-attachments/assets/e3bb4c5b-4fa8-4bc6-92d8-9e119e598698" />


JENKINS REPORT


<img width="1920" height="918" alt="jen report" src="https://github.com/user-attachments/assets/2e8046bf-bd65-491a-8f9f-935dab62de8d" />


SECURITY SCAN


<img width="1920" height="918" alt="jen scan" src="https://github.com/user-attachments/assets/a59fd702-959f-4f4d-a80e-b6096fa84848" />


JENKINS SUCCESS


<img width="1920" height="918" alt="jen success" src="https://github.com/user-attachments/assets/ab6eeb97-443b-4cc6-a7ef-a063e8060e21" />



# Installation

``` bash
git clone https://github.com/manishgowda17/enterprise-devops-project.git
cd enterprise-devops-project
docker compose -f docker/docker-compose.yml up -d --build
```

Access:

http://`<EC2_PUBLIC_IP>`{=html}:5000

# Jenkins Pipeline

Stages:

1.  Checkout Source Code
2.  Verify Docker
3.  Build Docker Image
4.  Deploy Application
5.  AI Build Summary
6.  Health Check
7.  Archive Reports
8.  Cleanup

# DevSecOps

-   validate.sh validates project structure.
-   security_scan.sh performs lightweight security checks.
-   aibuild.py generates build summaries.

# Health Monitoring

Endpoints:

-   /
-   /health
-   /version
-   /metrics

# Reports

Generated reports:

-   deployment_report.txt
-   security_report.txt

# Resume Highlights

-   Built a complete CI/CD pipeline.
-   Automated Docker deployments.
-   Integrated validation and security scripts.
-   Implemented AI build reporting.
-   Deployed on AWS EC2.
-   Added health monitoring and deployment reports.

# Author

**Manish Gowda S N**

DevOps Engineer \| AWS \| Docker \| Jenkins \| Python \| Linux

# License

MIT License

If this repository helped you, please ⭐ star it.
  
