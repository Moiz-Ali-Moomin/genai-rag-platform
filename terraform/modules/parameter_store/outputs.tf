output "parameter_arn" {
  value = aws_ssm_parameter.openai_api_key.arn
}

output "parameter_name" {
  value = aws_ssm_parameter.openai_api_key.name
}
