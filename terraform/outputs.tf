output "data_lake_bucket" {
  value       = var.data_lake_bucket
  description = "S3 data lake bucket"
}

output "scripts_bucket" {
  value       = var.scripts_bucket
  description = "Glue scripts bucket"
}
