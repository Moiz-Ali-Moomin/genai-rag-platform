# RAG Pipeline Design

The platform uses a scalable RAG (Retrieval-Augmented Generation) pipeline entirely managed by AWS Bedrock for the storage and retrieval phase, and OpenAI for the synthesis phase.

## 1. Document Ingestion
1. Documents (PDFs, Word docs, text) are uploaded to an **Amazon S3 Bucket**.
2. **AWS Bedrock Knowledge Bases** is configured with an S3 data source.
3. Bedrock automatically divides the documents into chunks and generates embeddings.
4. The embeddings are stored in an **Amazon OpenSearch Serverless** vector index.

## 2. Retrieval Retrieval Phase
1. The user provides a query via the API.
2. The `rag/retrievers.py` wrapper uses the `Retrieve` API from AWS Bedrock to search the Knowledge Base.
3. Relevant text chunks (context) are returned based on cosine similarity in OpenSearch.

## 3. Augmentation & Generation Phase
1. The `RAGAgent` in `agents/rag_agent.py` takes the original query and the retrieved context.
2. It structures a prompt (e.g., "Answer based on context: [context], Question: [query]").
3. The prompt is sent to the LLM (OpenAI GPT-4).
4. The concise, grounded answer is returned to the user.
