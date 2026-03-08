# Deployment Guide

The platform uses Infrastructure as Code (IaC) via **Terraform** and CI/CD via **GitHub Actions**.

## Prerequisites
- AWS CLI configured with administrative access.
- Terraform CLI (>= 1.5.0) installed.
- Docker installed locally.

## Deploying Infrastructure
1. Navigate to the `terraform/` directory.
2. Edit or create the appropriate `dev.tfvars` or `prod.tfvars` in `terraform/environments/` with your variables (e.g., `openai_api_key`).
3. Initialize the directory:
   ```bash
   terraform init
   ```
4. Apply the configuration:
   ```bash
   terraform apply -var-file="environments/dev.tfvars"
   ```

## CI/CD Pipeline
- **CI (`ci.yml`)**: On every Pull Request and push to `main`, the code is linted (`ruff`) and tested (`pytest`). A Docker image build is validated.
- **CD (`cd.yml`)**: On every tagged release (`v*`), the Docker image is built, pushed to **Amazon ECR**, and automatically deployed to **AWS App Runner**.

## Local Development
To run locally without deploying:
1. Copy `.env.example` to `.env` and fill the variables.
2. Run `make setup`
3. Run `make dev-api` to start FastAPI on `http://localhost:8000`.
4. Run `make dev-ui` to start Gradio on `http://localhost:8080`.
