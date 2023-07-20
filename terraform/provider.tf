provider "google" {
  project     = "opendota-data-pipeline"
  region      = "us-east1"
}


terraform {
  backend "gcs" {
    bucket  = "opendota-terraform"
    prefix  = "terraform/state"
  }
}