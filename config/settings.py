from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional
from functools import lru_cache

class Settings(BaseSettings):
    """
    Application settings, loaded from environment variables and .env file.
    """
    # Environment
    app_env: str = "development"
    log_level: str = "INFO"

    # AWS
    aws_default_region: str = "us-east-1"
    aws_profile: Optional[str] = None
    bedrock_knowledge_base_id: str

    # OpenAI
    openai_api_key: str
    openai_model: str = "gpt-4"

    # API Server
    api_host: str = "0.0.0.0"
    api_port: int = 8000

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        # Allow extra fields in the environment that are not defined here
        extra="ignore"
    )

@lru_cache()
def get_settings() -> Settings:
    """
    Get cached settings instance.
    """
    return Settings()
