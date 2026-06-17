terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
    }
  }
}

provider "google" {
  project = "shopworld-demo"
  region  = "europe-west1"
}
