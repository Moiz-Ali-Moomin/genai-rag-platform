import boto3
import json
import time
from opensearchpy import OpenSearch, RequestsHttpConnection, AWSV4SignerAuth

region = 'us-east-1'
collection_name = 'genai-rag-dev-vector-db'

# Get collection endpoint
client = boto3.client('opensearchserverless', region_name=region)
response = client.batch_get_collection(names=[collection_name])
try:
    host = response['collectionDetails'][0]['collectionEndpoint'].replace('https://', '')
except IndexError:
    print(f"Collection {collection_name} not found.")
    exit(1)

# Set up auth
credentials = boto3.Session().get_credentials()
auth = AWSV4SignerAuth(credentials, region, 'aoss')

# Create index
os_client = OpenSearch(
    hosts=[{'host': host, 'port': 443}],
    http_auth=auth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)

index_name = 'bedrock-knowledge-base-default-index'
index_body = {
    "settings": {
        "index.knn": True
    },
    "mappings": {
        "properties": {
            "bedrock-embedding": {
                "type": "knn_vector",
                "dimension": 1024, # Titan V2 Text Embedding size
                "method": {
                    "name": "hnsw",
                    "engine": "faiss",
                    "space_type": "l2"
                }
            },
            "AMAZON_BEDROCK_METADATA": {
                "type": "text",
                "index": False
            },
            "AMAZON_BEDROCK_TEXT_CHUNK": {
                "type": "text",
                "index": True
            }
        }
    }
}

try:
    response = os_client.indices.create(index=index_name, body=index_body)
    print("Index created:", response)
except Exception as e:
    print("Error creating index:", e)
