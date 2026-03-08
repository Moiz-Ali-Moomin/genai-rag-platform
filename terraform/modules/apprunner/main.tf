data "aws_region" "current" {}

# ==========================================
# App Runner Service
# ==========================================
resource "aws_apprunner_auto_scaling_configuration_version" "this" {
  auto_scaling_configuration_name = "${var.service_name}-autoscaling"
  max_concurrency = 100
  max_size        = 10
  min_size        = 1
}

# Ensure the Docker image is pushed BEFORE creating the App Runner service
resource "aws_apprunner_service" "this" {
  service_name = var.service_name

  source_configuration {
    auto_deployments_enabled = true
    authentication_configuration {
      access_role_arn = var.access_role_arn
    }

    image_repository {
      image_configuration {
        port = "8000"
        
        runtime_environment_variables = {
          AWS_DEFAULT_REGION        = var.aws_region
          BEDROCK_KNOWLEDGE_BASE_ID = var.bedrock_knowledge_base_id
          OPENAI_MODEL              = "gpt-4"
        }
        
        runtime_environment_secrets = {
          OPENAI_API_KEY = var.openai_api_key_parameter_arn
        }
      }
      image_identifier      = "${var.ecr_repository_url}:latest"
      image_repository_type = "ECR"
    }
  }

  instance_configuration {
    cpu               = "2048" # 2 vCPU
    memory            = "4096" # 4 GB
    instance_role_arn = var.instance_role_arn
  }

  health_check_configuration {
    healthy_threshold   = 1
    unhealthy_threshold = 5
    timeout             = 5
    interval            = 10
    protocol            = "HTTP"
    path                = "/"
  }

  auto_scaling_configuration_arn = aws_apprunner_auto_scaling_configuration_version.this.arn
}
