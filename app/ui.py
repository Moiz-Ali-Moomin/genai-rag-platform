import gradio as gr
from models.chat import ChatRequest
from agents.rag_agent import get_rag_agent
from config.settings import get_settings
from utils.logger import setup_logger

logger = setup_logger(__name__)
settings = get_settings()

def chat_interface(message, history):
    """
    Gradio chat interface function.
    """
    try:
        agent = get_rag_agent()
        # Create request model (ignoring history for simplicity in this iteration,
        # but the schema allows future expansion)
        request = ChatRequest(message=message)
        
        # In a real deployed split architecture, this would make an HTTP call to the API.
        # Calling agent directly to keep consistent with local deployment needs.
        response = agent.generate_response(request)
        
        if response.error:
            return f"An error occurred: {response.error}"
            
        return response.response
        
    except Exception as e:
        logger.error(f"Error during Gradio chat generation: {e}")
        return f"An unexpected system error occurred: {str(e)}"

# Define Gradio Interface
demo = gr.ChatInterface(
    fn=chat_interface,
    title="GenAI RAG Platform",
    description="Enterprise document retrieval and chat interface powered by AWS Bedrock and OpenAI.",
    examples=[
        "What are the main topics of the documents?", 
        "Summarize the key findings."
    ]
)

if __name__ == "__main__":
    logger.info(f"Starting UI on port {settings.api_port}")
    demo.launch(server_name=settings.api_host, server_port=settings.api_port)
