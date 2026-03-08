output "collection_id" {
  value = aws_opensearchserverless_collection.vector_store.id
}

output "collection_arn" {
  value = aws_opensearchserverless_collection.vector_store.arn
}

output "collection_endpoint" {
  value = aws_opensearchserverless_collection.vector_store.collection_endpoint
}
