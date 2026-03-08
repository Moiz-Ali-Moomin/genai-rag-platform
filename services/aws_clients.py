import boto3
from config.settings import get_settings
from utils.logger import setup_logger

logger = setup_logger(__name__)
settings = get_settings()

class AWSClientFactory:
    """
    Factory class to create and manage boto3 clients.
    """
    @staticmethod
    def get_boto3_session():
        try:
            if settings.aws_profile:
                return boto3.Session(
                    profile_name=settings.aws_profile,
                    region_name=settings.aws_default_region
                )
            else:
                return boto3.Session(
                    region_name=settings.aws_default_region
                )
        except Exception as e:
            logger.error(f"Failed to create boto3 session: {e}")
            raise

    @classmethod
    def get_client(cls, service_name: str):
        session = cls.get_boto3_session()
        return session.client(service_name)
        
    @classmethod
    def get_bedrock_agent_runtime(cls):
        return cls.get_client("bedrock-agent-runtime")
