variable "project_name" {
  description = "Base name for resources"
  type        = string
}

variable "repository_url" {
  description = "The URL of the ECR repository"
  type        = string
}

variable "repository_name" {
  description = "The name of the ECR repository"
  type        = string
}

variable "codebuild_role_arn" {
  description = "The ARN of the IAM role for CodeBuild"
  type        = string
}

variable "aws_region" {
  description = "The AWS region"
  type        = string
}

variable "s3_bucket_id" {
  description = "The ID of the S3 bucket containing the source"
  type        = string
}
