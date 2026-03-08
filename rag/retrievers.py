from llama_index.core.retrievers import BaseRetriever
from llama_index.retrievers.bedrock import AmazonKnowledgeBasesRetriever
from config.settings import get_settings
from utils.logger import setup_logger

logger = setup_logger(__name__)
settings = get_settings()

def get_bedrock_retriever() -> BaseRetriever:
    """
    Initializes and returns the Amazon Bedrock Knowledge Bases Retriever.
    """
    try:
        retriever = AmazonKnowledgeBasesRetriever(
            knowledge_base_id=settings.bedrock_knowledge_base_id,
            retrieval_config={
                "vectorSearchConfiguration": {
                    "numberOfResults": 3
                }
            },
            region_name=settings.aws_default_region,
        )
        logger.info(f"Initialized Bedrock KB Retriever for KB ID: {settings.bedrock_knowledge_base_id}")
        return retriever
    except Exception as e:
        logger.error(f"Failed to initialize Bedrock KB Retriever: {e}")
        raise
