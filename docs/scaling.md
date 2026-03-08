# Platform Scaling Rules

The GenAI RAG Platform is designed for scale. Given the stateless nature of the RAG Application, horizontal scalability is native.

## Web Server (AWS App Runner)
- **Auto-Scaling**: App Runner scales the container instances based on concurrent HTTP requests count. The threshold is configurable in `cd.yml`.
- **Max concurrency**: 100 requests per instance by default. AppRunner provisions new containers when traffic spikes.

## Storage (S3 & OpenSearch)
- **Amazon S3**: Practically limitless storage for document ingestion.
- **Amazon OpenSearch Serverless**: Automatically provisions and scales OCU (OpenSearch Compute Units) from 2 to x based on indexing workload and query volume.

## LLM Gateway (OpenAI / Bedrock)
- Ensure your configured API endpoints have adequate rate limits (Token per minute / Requests per minute).
- Adding caching (e.g., Redis via LangChain/LlamaIndex) for identical queries will drastically reduce token consumption at scale.
