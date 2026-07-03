#!/bin/bash

set -e

echo "===== Starting Deployment ====="

echo "Stopping old container..."
docker rm -f flask-app || true

echo "Starting new container..."
docker run -d \
  --name flask-app \
  -p 5001:5000 \
  yamini786/cicd-jenkins-pipeline:v2

echo "Waiting for application to start..."
sleep 5

echo "Checking running containers..."
docker ps

echo "===== Deployment Successful ====="