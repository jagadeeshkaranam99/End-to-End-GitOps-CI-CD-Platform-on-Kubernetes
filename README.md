# python-app

Containerized Python Flask REST API for End-to-End GitOps CI/CD Platform

## Overview
This repository contains a containerized Python Flask REST API designed to demonstrate end-to-end GitOps CI/CD practices. The infrastructure, Kubernetes manifests, Helm charts, and GitOps deployments are managed in the companion repository: [gitops-infra-manifests](https://github.com/jagadeeshkaranam99/gitops-infra-manifests).

## Architecture & CI/CD Pipeline

```
+------------------+         +----------------------------+         +-----------------------+
|  Developer Push  | ------> | GitHub Actions (CI/CD)     | ------> | Docker Hub Container  |
|  to 'main'       |         | - Build & Tag Docker Image |         | Registry              |
+------------------+         | - Update Infra Manifest    |         +-----------------------+
                             +----------------------------+                     |
                                           |                                    v
                                           v                            +-----------------------+
                             +----------------------------+             | Terraform AWS EKS     |
                             | gitops-infra-manifests Repo| <---------- | - ArgoCD Sync         |
                             +----------------------------+             | - Traefik Gateway API |
                                                                        | - Prometheus/Grafana  |
                                                                        +-----------------------+
```

### End-to-End Flow
1. **Application Code Changes**: Pushing code updates to `main` triggers GitHub Actions CI pipeline.
2. **Container Build & Publish**: Docker image is built and pushed to Docker Hub tagged with the short Git commit SHA.
3. **GitOps Manifest Update**: GitHub Actions automatically updates the Helm chart image tag in [gitops-infra-manifests](https://github.com/jagadeeshkaranam99/gitops-infra-manifests).
4. **GitOps Synchronization**: ArgoCD monitors `gitops-infra-manifests` and synchronizes changes to the AWS EKS cluster automatically.

## Infrastructure & Stack Overview

- **Cloud & Orchestration**: AWS EKS provisioned with Terraform.
- **Ingress & Routing**: Traefik Gateway API managing ingress traffic to application services.
- **GitOps Continuous Delivery**: ArgoCD continuously reconciling cluster state with manifest repository declarations.
- **Observability & Monitoring**: Prometheus for metrics collection and Grafana for dashboards/alerts.

## Tech Stack
- **Language**: Python 3.13.3
- **Framework**: Flask 3.0.3
- **Containerization**: Docker
- **Orchestration**: Kubernetes / AWS EKS / ArgoCD / Traefik Gateway API

## Companion Infrastructure Repository
Infrastructure code, Helm charts, Traefik Gateway API configurations, and ArgoCD applications reside in [gitops-infra-manifests](https://github.com/jagadeeshkaranam99/gitops-infra-manifests).

## API Endpoints
- `GET /api/v1/info` - Returns service info and metadata
- `GET /api/v1/healthz` - Returns health status
