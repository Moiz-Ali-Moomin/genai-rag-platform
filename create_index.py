import sys
import subprocess

def install_deps():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "boto3", "requests", "requests-aws4auth"])

install_deps()

import boto3
import json
import requests
from requests_aws4auth import AWS4Auth

region = 'us-east-1'
service = 'aoss'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

client = boto3.client('opensearchserverless', region_name=region)

# The collection name is from dev.tfvars -> genai-rag-dev-vector-db
collections = client.list_collections()['collectionSummaries']
collection = next((c for c in collections if c['name'] == 'genai-rag-dev-vector-db'), None)
if not collection:
    print("Collection genai-rag-dev-vector-db not found!")
    exit(1)

host = collection.get('collectionEndpoint')
if not host:
    collection_details = client.batch_get_collection(ids=[collection['id']])['collectionDetails'][0]
    host = collection_details.get('collectionEndpoint')

if not host.startswith('https://'):
    host = 'https://' + host

print(f"Host: {host}")

index_name = 'bedrock-knowledge-base-default-index'
url = host + '/' + index_name

payload = {
  "settings": {
    "index": {
      "knn": True,
      "knn.algo_param.ef_search": 512
    }
  },
  "mappings": {
    "properties": {
      "bedrock-embedding": {
        "type": "knn_vector",
        "dimension": 1024,
        "method": {
          "name": "hnsw",
          "engine": "nmslib",
          "space_type": "cosinesimil"
        }
      },
      "AMAZON_BEDROCK_TEXT_CHUNK": {
        "type": "text",
        "index": True
      },
      "AMAZON_BEDROCK_METADATA": {
        "type": "text",
        "index": False
      }
    }
  }
}

headers = {"Content-Type": "application/json"}
print("Creating index...")
response = requests.put(url, auth=awsauth, json=payload, headers=headers)
print(response.status_code)
print(response.text)
