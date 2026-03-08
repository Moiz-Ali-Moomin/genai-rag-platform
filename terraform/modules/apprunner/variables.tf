variable "service_name" {
  description = "Name of the App Runner service"
  type        = string
}

variable "ecr_repository_url" {
  description = "ECR repository URL"
  type        = string
}

variable "instance_role_arn" {
  description = "ARN of the IAM role that provides permissions to your App Runner service"
  type        = string
}

variable "access_role_arn" {
  description = "ARN of the IAM role that provides permissions to App Runner to access ECR"
  type        = string
}

variable "aws_region" {
  description = "AWS region"
  type        = string
}

variable "bedrock_knowledge_base_id" {
  description = "Bedrock KB ID"
  type        = string
}

variable "openai_api_key_parameter_arn" {
  description = "ARN of the SSM Parameter storing the OpenAI API Key"
  type        = string
}

variable "docker_dir" {
  description = "Path to the directory containing the Dockerfile"
  type        = string
}
