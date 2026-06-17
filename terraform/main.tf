terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 6.0"
    }
  }
}

provider "google" {
  project = "shopworld-demo"
  region  = "europe-west1"
}

variable "project_id" {
  default = "shopworld-demo"
}

variable "region" {
  default = "europe-west1"
}

# This Terraform folder documents the ShopWorld cloud architecture:
# - Cloud Run frontend
# - Cloud Run backend
# - Cloud SQL MySQL
# - Cloud Storage product images
# - BigQuery analytics
# - Cloud Monitoring dashboard
# - Firebase Authentication
