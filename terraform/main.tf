data "aws_caller_identity" "current" {}

module "s3" {
  source      = "./modules/s3"
  bucket_name = "${var.project_name}-docs-${data.aws_caller_identity.current.account_id}"
}

module "ecr" {
  source          = "./modules/ecr"
  repository_name = var.project_name
}

module "parameter_store" {
  source               = "./modules/parameter_store"
  openai_api_key_value = var.openai_api_key
}

module "opensearch" {
  source          = "./modules/opensearch"
  collection_name = "${var.project_name}-vector-db"
  principal_arns  = [module.iam.bedrock_role_arn]

  depends_on = [module.iam]
}

module "iam" {
  source                    = "./modules/iam"
  s3_bucket_arn             = module.s3.bucket_arn
  openai_key_arn            = module.parameter_store.parameter_arn

  depends_on = [module.s3, module.parameter_store]
}

module "bedrock" {
  source                    = "./modules/bedrock"
  knowledge_base_name       = "${var.project_name}-kb"
  s3_bucket_arn             = module.s3.bucket_arn
  opensearch_collection_arn = module.opensearch.collection_arn
  bedrock_role_arn          = module.iam.bedrock_role_arn

  depends_on = [module.s3, module.opensearch, module.iam]
}

module "codebuild" {
  source             = "./modules/codebuild"
  project_name       = var.project_name
  repository_url     = module.ecr.repository_url
  repository_name    = var.project_name
  codebuild_role_arn = module.iam.codebuild_role_arn
  aws_region         = var.aws_region
  s3_bucket_id       = module.s3.bucket_id

  depends_on = [module.ecr, module.iam, module.s3]
}

module "apprunner" {
  source                       = "./modules/apprunner"
  service_name                 = "${var.project_name}-app"
  ecr_repository_url           = module.ecr.repository_url
  instance_role_arn            = module.iam.apprunner_instance_role_arn
  access_role_arn              = module.iam.apprunner_access_role_arn
  aws_region                   = var.aws_region
  bedrock_knowledge_base_id    = module.bedrock.knowledge_base_id
  openai_api_key_parameter_arn = module.parameter_store.parameter_arn
  docker_dir                   = "${path.root}/../" # Points to the parent directory containing the docker/ directory

  depends_on = [module.iam, module.ecr, module.bedrock, module.parameter_store, module.codebuild]
}
