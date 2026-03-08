resource "aws_ssm_parameter" "openai_api_key" {
  name        = "/chatbot/openai_api_key"
  description = "OpenAI API Key for GenAI RAG Chatbot"
  type        = "SecureString"
  value       = var.openai_api_key_value
}
