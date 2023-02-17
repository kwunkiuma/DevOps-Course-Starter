terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = ">= 3.8"
    }
  }

  backend "azurerm" {
      resource_group_name  = "Softwire21_FrankMa_ProjectExercise"
      storage_account_name = "framaswstorage"
      container_name       = "framasw-container"
      key                  = "terraform.tfstate"
  }
}

provider "azurerm" {
  features {}
}

data "azurerm_resource_group" "main" {
  name                = "Softwire21_FrankMa_ProjectExercise"
}

resource "azurerm_service_plan" "main" {
  name                = "${var.prefix}-terraformed-asp"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  os_type             = "Linux"
  sku_name            = "B1"
}

resource "azurerm_linux_web_app" "main" {
  name                = "framasw-tf"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  service_plan_id     = azurerm_service_plan.main.id

  site_config {
    application_stack {
      docker_image     = "framasw/todo-app"
      docker_image_tag = "latest"
    }
  }

  app_settings = {
    "DOCKER_REGISTRY_SERVER_URL" = "https://index.docker.io"
    "FLASK_APP"  =  "todo_app/app"
    "SECRET_KEY"  =  "${var.secret_key}"
    "COSMOSDB_URL"  =  azurerm_cosmosdb_account.main.endpoint
    "COSMOSDB_PRIMARY_CONNECTION_STRING"  =  azurerm_cosmosdb_account.main.connection_strings[0]
    "LOGIN_DISABLED"  =  "True"
    "GITHUB_OAUTH_CLIENT_ID"  =  "${var.github_oauth_client_id}"
    "GITHUB_OAUTH_CLIENT_SECRET"  =  "${var.github_oauth_client_secret}"
    "GITHUB_OAUTH_REDIRECT_URI"  =  "https://framasw-tf.azurewebsites.net/login/callback"
  }
}

resource "azurerm_cosmosdb_account" "main" {
  name                = "${var.prefix}-framasw-tf-cosmos-db-account"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  offer_type          = "Standard"
  kind                = "MongoDB"
  mongo_server_version = 4.2

  capabilities {
    name = "EnableMongo"
  }
  
  capabilities {
    name = "EnableServerless"
  }

  consistency_policy {
    consistency_level       = "BoundedStaleness"
    max_interval_in_seconds = 300
    max_staleness_prefix    = 100000
  }

  geo_location {
    location          = data.azurerm_resource_group.main.location
    failover_priority = 0
  }
}

resource "azurerm_cosmosdb_mongo_database" "main" {
  name                = "${var.prefix}-framasw-tf-cosmos-mongo-db"
  resource_group_name = azurerm_cosmosdb_account.main.resource_group_name
  account_name        = azurerm_cosmosdb_account.main.name
  lifecycle {
    prevent_destroy = true 
  }
}