variable "s3_bucket_arn" {
  description = "ARN of the S3 bucket"
  type        = string
}


variable "openai_key_arn" {
  description = "ARN of the Parameter Store containing OpenAI API Key"
  type        = string
}
