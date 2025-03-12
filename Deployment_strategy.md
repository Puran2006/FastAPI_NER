# Deploying FastAPI NER on AWS

This guide covers deploying the FastAPI-based Named Entity Recognition (NER) API on **AWS**:

## **EC2 (Elastic Compute Cloud) with Docker**

### 1️⃣ Set Up an AWS EC2 Instance
1. Log in to your AWS account.
2. Go to **EC2 Dashboard** → Click **Launch Instance**.
3. Select **Ubuntu 20.04 LTS** (or any other preferred OS).
4. Choose an instance type (Recommended: `t3.small` or higher).
5. Configure security group:
   - Allow **port 22 (SSH)** for remote access.
   - Allow **port 8000 (FastAPI)** for API access.
6. Launch and download the key-pair (`.pem`) file for SSH access.

### 2️⃣ Connect to EC2 via SSH
```sh
ssh -i your-key.pem ubuntu@your-ec2-instance-ip
```

### 3️⃣ Install Required Packages
```sh
sudo apt update && sudo apt upgrade -y
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
```

### 4️⃣ Pull and Run Docker Image
If you have already pushed your Docker image to **Docker Hub**, pull it directly:

puran2006 is my dockerhub
```sh
docker pull puran2006/fastapi-app:latest
```
Run the container:
```sh
docker run -d -p 8000:8000 puran2006/fastapi-app:latest
```
Your API will be available at:
- `http://your-ec2-instance-ip:8000`

To keep the service running after disconnecting SSH:
```sh
docker run -d --restart unless-stopped -p 8000:8000 puran2006/fastapi-app:latest
```
---
