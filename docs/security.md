# Security Architecture

## IAM and Least Privilege
Every AWS component operates with the principle of least privilege:
- **AppRunner Instance Role**: Only allowed to call Bedrock's `Retrieve` API and read from AWS Systems Manager Parameter Store.
- **Bedrock Role**: Allowed to read from the specific S3 bucket and write embeddings to the designated OpenSearch collection.

## Secrets Management
- The `OPENAI_API_KEY` is completely removed from the environment codebase. It is provisioned natively in AWS Systems Manager Parameter Store.
- AppRunner loads it securely at runtime into the container environment.

## Container Security
- The Dockerfile employs a multi-stage build, compiling dependencies in a builder stage and copying only the artifacts.
- A non-root user (`appuser`) executes the Python process, mitigating privilege escalation risks.

## Data in Transit and Rest
- AppRunner automatically enforces TLS on incoming requests (HTTPS).
- Bedrock Knowledge Base and OpenSearch encrypt embeddings at rest using AWS KMS.
