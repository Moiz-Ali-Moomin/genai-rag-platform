from pydantic import BaseModel, Field
from typing import List, Optional

class Message(BaseModel):
    """
    A single message in a chat history.
    """
    role: str = Field(..., description="The role of the message sender (user or assistant)")
    content: str = Field(..., description="The content of the message")

class ChatRequest(BaseModel):
    """
    Request model for the chat endpoint.
    """
    message: str = Field(..., description="The user's input message")
    history: Optional[List[Message]] = Field(default_factory=list, description="Previous chat history")

class ChatResponse(BaseModel):
    """
    Response model for the chat endpoint.
    """
    response: str = Field(..., description="The generated response from the RAG agent")
    error: Optional[str] = Field(default=None, description="Error message if any")
