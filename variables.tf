variable "prefix" {
  description = "The prefix used for all resources in this environment"
}

variable "secret_key" {
  description = "Secret Key for encryption"
  sensitive   = true
}

variable "github_oauth_client_id" {
  description = "Github OAuth client id"
}

variable "github_oauth_client_secret" {
  description = "OAuth client secret"
  sensitive = true
}
