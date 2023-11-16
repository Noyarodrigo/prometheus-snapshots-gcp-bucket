module "prometheus_bucket" {
    source     = "./gcp-bucket"
    bucket_name   = "prometheus-bucket"
    storage_class = "REGIONAL"
    project_id = "${var.project_id}"
    region = "${var.region}"
}
