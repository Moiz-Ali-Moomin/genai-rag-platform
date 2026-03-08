variable "repository_name" {
  description = "Name of the ECR repository"
  type        = string
}

variable "force_delete" {
    type = bool
    default = true
}
