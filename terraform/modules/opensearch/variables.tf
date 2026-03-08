variable "collection_name" {
  description = "Name of the OpenSearch Serverless collection"
  type        = string
}

variable "principal_arns" {
  description = "List of IAM principal ARNs that require access to the OpenSearch collection data"
  type        = list(string)
}
