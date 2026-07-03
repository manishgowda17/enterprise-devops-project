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

Day 4 - Enterprise AI-Powered CI/CD Pipeline
Developer
      │
      ▼
 GitHub Repository
      │
      ▼
 Jenkins Pipeline
      │
      ├────────► Build Docker Image
      │
      ├────────► Validate Docker Compose
      │
      ├────────► Deploy Automatically
      │
      ├────────► Generate Build Report
      │
      ▼
 Running Application
