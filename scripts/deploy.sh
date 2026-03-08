#!/bin/bash
set -e

echo "Starting deployment to AWS..."

# Requires AWS credentials to be configured
if [ -z "$AWS_PROFILE" ] && [ -z "$AWS_ACCESS_KEY_ID" ]; then
    echo "Error: AWS credentials not found. Please setup AWS credentials."
    exit 1
fi

# Apply terraform infrastructure
echo "Applying Terraform configuration..."
cd terraform
terraform init
terraform apply -auto-approve

echo "Deployment completed successfully! Check Terraform outputs for accessing your app."
