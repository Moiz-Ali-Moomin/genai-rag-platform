variable "knowledge_base_name" {
  description = "Name of the Bedrock Knowledge Base"
  type        = string
}

variable "s3_bucket_arn" {
  description = "ARN of the S3 bucket used as the data source"
  type        = string
}

variable "opensearch_collection_arn" {
  description = "ARN of the OpenSearch Serverless collection"
  type        = string
}

variable "opensearch_vector_index_name" {
  description = "Name of the vector index in OpenSearch"
  type        = string
  default     = "bedrock-knowledge-base-default-index"
}

variable "bedrock_role_arn" {
  description = "ARN of the IAM role for Bedrock to use"
  type        = string
}
