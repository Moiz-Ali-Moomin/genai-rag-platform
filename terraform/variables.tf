variable "aws_region" {
  description = "AWS region to deploy to"
  type        = string
  default     = "us-east-1"
}

variable "openai_api_key" {
  description = "OpenAI API Key (passed via TF_VAR_openai_api_key or terraform.tfvars)"
  type        = string
  sensitive   = true
}

variable "project_name" {
  description = "Base name for resources"
  type        = string
  default     = "genai-chatbot"
}
