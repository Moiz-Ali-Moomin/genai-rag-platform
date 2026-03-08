resource "aws_codebuild_project" "this" {
  name          = "${var.project_name}-build"
  description   = "Builds the Docker image for the GenAI RAG chatbot and pushes it to ECR"
  build_timeout = "10" 
  service_role  = var.codebuild_role_arn

  artifacts {
    type = "NO_ARTIFACTS"
  }

  environment {
    compute_type                = "BUILD_GENERAL1_SMALL"
    image                       = "aws/codebuild/amazonlinux2-x86_64-standard:5.0"
    type                        = "LINUX_CONTAINER"
    privileged_mode             = true # Required for Docker build

    environment_variable {
      name  = "AWS_DEFAULT_REGION"
      value = var.aws_region
    }

    environment_variable {
      name  = "REPOSITORY_URL"
      value = var.repository_url
    }

    environment_variable {
      name  = "REPOSITORY_NAME"
      value = var.repository_name
    }
  }

  source {
    type      = "S3"
    location  = "${var.s3_bucket_id}/source/genai-chatbot.zip"
  }
}
