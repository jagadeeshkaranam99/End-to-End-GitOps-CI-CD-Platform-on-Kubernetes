# python-app

Containerized Python Flask REST API for End-to-End GitOps CI/CD Platform

## Overview
This repository contains a containerized Python Flask REST API designed to demonstrate end-to-end GitOps CI/CD practices.

## Architecture
```
[ Client / Gateway ] -> [ Traefik Gateway API ] -> [ Flask REST Service ] (Port 5000)
```

## Tech Stack
- **Language**: Python 3.13.3
- **Framework**: Flask 3.0.3
- **Containerization**: Docker
- **Orchestration**: Kubernetes / Kind / ArgoCD

## API Endpoints
- `GET /api/v1/info` - Returns service info and metadata
- `GET /api/v1/healthz` - Returns health status

## Local & Docker Setup

### Local Setup
```bash
pip install -r requirements.txt
python src/app.py
```

### Docker Setup
```bash
docker build -t python-app .
docker run -p 5000:5000 python-app
```

## CI/CD Workflow Details
1. Push code changes to `python-app`.
2. CI pipeline builds container image with `Dockerfile`.
3. ArgoCD tracks `infra-repo` and deploys updated Kubernetes manifests.
