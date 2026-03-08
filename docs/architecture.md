# System Architecture

The GenAI RAG Platform is built using a clean, modular architecture, segregating the infrastructure, API, and UI layers.

## High-Level Flow

```mermaid
graph TD
    Client[User / Browser] -->|HTTP POST| UI[Gradio UI (app/ui.py)]
    UI -->|HTTP POST| API[FastAPI (api/main.py)]
    API -->|Injects| Agent[RAG Agent (agents/rag_agent.py)]
    Agent -->|Retrieval| Retriever[Bedrock Retriever (rag/retrievers.py)]
    Retriever -->|Query| KB[AWS Bedrock Knowledge Base]
    KB -->|Search| OS[Amazon OpenSearch Serverless]
    OS -->|Results| KB
    KB -->|Context| Retriever
    Retriever -->|Context| Agent
    Agent -->|Prompt + Context| LLM[OpenAI API (services/llm_provider.py)]
    LLM -->|Generated Answer| Agent
    Agent -->|Response| API
    API -->|Response| UI
    UI -->|Response| Client
```

## Component Details

### `app/` (User Interface)
The entry point for end-users, built with Gradio. Connects to the backend API or directly calls the orchestrator agent for simplified local development.

### `api/` (Application Programming Interface)
FastAPI application that defines REST endpoints (`/chat/generate`). Uses Pydantic for validation and serialization.

### `agents/` (Orchestration)
Houses the core intelligence of the platform. The `RAGAgent` combines retrievers and LLMs using LlamaIndex constructs (`RetrieverQueryEngine`).

### `rag/` (Retrieval-Augmented Generation)
Contains abstractions for document retrieval, specifically mapping to Amazon Bedrock Knowledge Bases.

### `services/` (External Services)
Connects to external APIs and managed infrastructure. The `aws_clients.py` creates reusable Boto3 sessions, and `llm_provider.py` connects to OpenAI (or Bedrock Claude as needed).

### `config/` (Configuration Management)
Centralized configuration loaded from environment variables and AWS Parameter Store using `pydantic-settings`.
