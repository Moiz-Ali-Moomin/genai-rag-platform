from llama_index.llms.openai import OpenAI
from config.settings import get_settings
from utils.logger import setup_logger

logger = setup_logger(__name__)
settings = get_settings()

def get_llm_provider() -> OpenAI:
    """
    Initializes and returns the OpenAI LLM instance.
    """
    try:
        llm = OpenAI(
            model=settings.openai_model,
            api_key=settings.openai_api_key
        )
        logger.info(f"Initialized LLM provider with model: {settings.openai_model}")
        return llm
    except Exception as e:
        logger.error(f"Failed to initialize LLM Provider: {e}")
        raise
