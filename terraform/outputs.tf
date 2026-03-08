output "app_url" {
  description = "The URL of the deployed AppRunner application"
  value       = module.apprunner.service_url
}

output "s3_bucket_name" {
  description = "The S3 bucket where documents should be uploaded"
  value       = module.s3.bucket_id
}
