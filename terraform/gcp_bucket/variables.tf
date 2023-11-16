variable "bucket_name" {
  type = string
  description = "The name of our bucket"
}

variable "storage_class" {
  type = string
}

variable "project_id" {
  description = "The project ID to host the cluster in"
}

variable "region" {
  description = "The region to host the cluster in"
}
