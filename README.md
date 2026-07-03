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

1. Checkout Source Code
2. Build Docker Image
3. Docker Login
4. Push Image to Docker Hub
5. Deploy Application

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
