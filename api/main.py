from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from config.settings import get_settings
from models.chat import ChatRequest, ChatResponse
from agents.rag_agent import get_rag_agent, RAGAgent
from utils.logger import setup_logger

logger = setup_logger(__name__)
settings = get_settings()

app = FastAPI(
    title="GenAI RAG Platform API",
    description="API for navigating Knowledge Bases with GenAI Document Retrieval",
    version="1.0.0",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Root endpoint for health checks."""
    return {"message": "GenAI RAG Platform API is running"}

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}

@app.post("/chat/generate", response_model=ChatResponse)
async def generate_chat(
    request: ChatRequest, 
    agent: RAGAgent = Depends(get_rag_agent)
):
    """
    Generate a chat response using the RAG Agent.
    """
    logger.info("Received API request for /chat/generate")
    try:
        response = agent.generate_response(request)
        if response.error:
            raise HTTPException(status_code=500, detail=response.error)
        return response
    except Exception as e:
        logger.error(f"API Error in /chat/generate: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
