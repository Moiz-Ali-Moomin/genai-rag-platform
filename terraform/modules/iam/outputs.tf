output "bedrock_role_arn" {
  value = aws_iam_role.bedrock_knowledge_base.arn
}

output "apprunner_instance_role_arn" {
  value = aws_iam_role.apprunner_instance.arn
}

output "apprunner_access_role_arn" {
  value = aws_iam_role.apprunner_access.arn
}

output "codebuild_role_arn" {
  value = aws_iam_role.codebuild.arn
}
