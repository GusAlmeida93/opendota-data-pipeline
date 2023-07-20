resource "google_storage_bucket" "terraform" {
  name          = "opendota-terraform"
  location      = "us-east1"
  force_destroy = true

  public_access_prevention = "enforced"
}

resource "google_storage_bucket" "dataproc" {
  name          = "opendota-dataproc"
  location      = "us-east1"
  force_destroy = true

  public_access_prevention = "enforced"
}

resource "google_storage_bucket" "landing" {
  name          = "opendota-landing"
  location      = "us-east1"
  force_destroy = true

  public_access_prevention = "enforced"
}

resource "google_storage_bucket" "processing" {
  name          = "opendota-processing"
  location      = "us-east1"
  force_destroy = true

  public_access_prevention = "enforced"
}

resource "google_storage_bucket" "refined" {
  name          = "opendota-refined"
  location      = "us-east1"
  force_destroy = true

  public_access_prevention = "enforced"
}

