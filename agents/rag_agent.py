from llama_index.core.query_engine import RetrieverQueryEngine
from services.llm_provider import get_llm_provider
from rag.retrievers import get_bedrock_retriever
from utils.logger import setup_logger
from models.chat import ChatRequest, ChatResponse

logger = setup_logger(__name__)

class RAGAgent:
    """
    RAG Orchestrator agent that handles combining context retrieval and LLM generation.
    """
    def __init__(self):
        self.llm = get_llm_provider()
        self.retriever = get_bedrock_retriever()
        self.query_engine = RetrieverQueryEngine.from_args(
            retriever=self.retriever,
            llm=self.llm,
        )
        logger.info("RAGAgent initialized successfully.")

    def generate_response(self, request: ChatRequest) -> ChatResponse:
        """
        Takes the user prompt and history, retrieves relevant context from Bedrock KB,
        and generates an answer via OpenAI LLM.
        """
        try:
            logger.info(f"Generating response for prompt: {request.message}")
            
            # Formatting prompt with instructions (expandable for history later)
            formatted_prompt = f"Answer concisely based on the retrieved context. Question: {request.message}"
            
            response = self.query_engine.query(formatted_prompt)
            return ChatResponse(response=str(response))
        except Exception as e:
            logger.error(f"Error during response generation: {e}")
            return ChatResponse(response="", error=str(e))

# Singleton instance
_agent_instance = None

def get_rag_agent() -> RAGAgent:
    """
    Returns a singleton instance of the RAGAgent.
    """
    global _agent_instance
    if _agent_instance is None:
        _agent_instance = RAGAgent()
    return _agent_instance
