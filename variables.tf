variable "access_key" {}
variable "secret_key" {}
variable "region" {}
variable "circle_key" {}

variable "app_name" {
  description = "short name of this app"
  default = "tranmon"
}

variable "function_name" {
  description = "List of the name of the function for the handlers for which to create lambda functions - needs to match the list defined in terraform variable 'function_handler'"
  type = "list"
  default = ["market_handler_overview", "profitability_handler_all_currencies", "wallet_handler_overview"]
}

variable "function_handler" {
  description = "List of the handlers for which to create lambda functions"
  type = "list"
  default = ["market_handler.overview", "profitability_handler.all_currencies", "wallet_handler.overview"]
}

variable "function_runtime" {
  description = "Desired lambda runtime to use"
  default = "python2.7"
}
