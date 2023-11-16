resource "google_storage_bucket" "prometheus_bucket" {
  name          = var.bucket_name
  location      = var.region
  storage_class = var.storage_class

  force_destroy = true

  public_access_prevention = "enforced"

  versioning {
	enabled = true
      }

  lifecycle_rule {
    condition {
      age = 7
    }
    action {
      type = "Delete"
    }
  }

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}
