provider "aws" {
  region = "us-east-2"
}

# Centralizar o arquivo de controle de estado do terraform
terraform {
  backend "s3" {
    bucket = "terraform-state-igti-barbara"
    key    = "state/igti/edc/mod1/terraform.tfstate"
    region = "us-east-2"
  }
}