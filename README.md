# 🚀 CI/CD Pipeline Automation using Jenkins

## 📌 Project Overview

This project demonstrates an end-to-end CI/CD pipeline using Jenkins to automate the build, Docker image creation, Docker Hub push, and deployment of a Flask application.

Whenever the pipeline runs, Jenkins automatically:

- Checks out the latest source code from GitHub
- Builds a Docker image
- Logs into Docker Hub
- Pushes the latest image
- Deploys the application using a deployment script

---

## Architecture

```text
Developer
    │
    ▼
GitHub Repository
    │
    ▼
Jenkins Pipeline
    │
    ▼
Checkout Source Code
    │
    ▼
Build Docker Image
    │
    ▼
Docker Login
    │
    ▼
Push Image to Docker Hub
    │
    ▼
Execute deploy.sh
    │
    ▼
Docker Container
    │
    ▼
Flask Application (Port 5001)
```

---

## 🛠 Technologies Used

- Jenkins
- Git
- GitHub
- Docker
- Docker Hub
- Flask
- Linux Shell Script (deploy.sh)

---

## 📂 Project Structure

```
cicd-jenkins-pipeline-imp/
│
├── app.py
├── Dockerfile
├── deploy.sh
├── Jenkinsfile
├── requirements.txt
├── README.md
└── .dockerignore
```

---

## ⚙ Pipeline Workflow

1. Checkout source code from GitHub
2. Build the Docker image
3. Authenticate with Docker Hub
4. Push the Docker image to Docker Hub
5. Execute the deployment script
6. Deploy the updated Flask application

---

## 🚀 Deployment Process

The deployment script performs the following tasks:

- Stops the existing container
- Removes the old container
- Pulls/uses the latest Docker image
- Starts a new container
- Verifies the deployment

---

## 📦 Docker Image

Repository:

```
yamini786/cicd-jenkins-pipeline
```

---

## 🌐 Application

Flask Application runs on:

```
http://localhost:5001
```

---

## 📈 Jenkins Pipeline Stages

- Checkout
- Build Docker Image
- Docker Login
- Push Docker Image
- Deploy

---

## 📚 Skills Demonstrated

- CI/CD Pipeline Automation
- Jenkins Pipeline
- Jenkinsfile
- Docker Containerization
- Docker Hub Integration
- Git Version Control
- Automated Deployment
- Shell Scripting

---

## 👩‍💻 Author

Yamini Nelluru
