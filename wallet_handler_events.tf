variable "wallets" {
  description = "List of wallets"
  type = "list"
  default = [
    "ANQNEgvto89aLa8KLRLUMKiVbStF6MLFDd",
    "AQZ69kCuuVhMfRDbMo4kmmfiewhAPCtnHb",
    "AJX3UNSNa3rXFUfRyMQuM13Y2NZQbTbxvf",
    "Gd7PdM1ydc8TYJWTmymVyMgL6b4sgjod6L",
    "AGrrJNqhvfjyCMtsVRenCktLwS2kXNYXMq",
    "AR7GbTXV7a6muB2AroYXKfCMG4HK8QS2BH",
    "AeucgHfjCYnRz5LwkzpjWtW6z9QE1MEU7D",
    "AdwB3SxCDu5wxjZPUcJToCnamNcHLM5CBJ",
    "ASTp3dioccitrTgYYH82dVkoGGo1uneKZ6"
  ]
}
variable "currencies_for_wallets" {
  description = "List of currencies"
  type = "list"
  default = [
    "arc",
    "arc",
    "arc",
    "btg",
    "sono",
    "sono",
    "sono",
    "arc",
    "arc"
  ]
}

resource "aws_cloudwatch_event_rule" "wallet_handler_event_rule" {
  count            = "${length(var.wallets)}"
  name                = "wallet_${element(var.currencies_for_wallets, count.index)}_${element(var.wallets, count.index)}"
  description         = "Invoke ${element(aws_lambda_function.app_function.*.arn, 2)} every 5 mins"
  schedule_expression = "rate(5 minutes)"
}

resource "aws_lambda_permission" "wallet_handler_function_allow_cloud_watch" {
  count            = "${length(var.wallets)}"
  statement_id  = "AllowExecutionFromCloudWatch_${element(aws_cloudwatch_event_rule.wallet_handler_event_rule.*.name, count.index)}"
  action        = "lambda:InvokeFunction"
  function_name = "${element(aws_lambda_function.app_function.*.arn, 2)}"
  principal     = "events.amazonaws.com"
  source_arn    = "${element(aws_cloudwatch_event_rule.wallet_handler_event_rule.*.arn, count.index)}"
}

resource "aws_cloudwatch_event_target" "wallet" {
  count            = "${length(var.currencies_for_wallets)}"
  rule  = "${element(aws_cloudwatch_event_rule.wallet_handler_event_rule.*.id, count.index)}"
  arn  = "${element(aws_lambda_function.app_function.*.arn, 2)}"
  input =  <<EOF
{
  "address": "${element(var.wallets, count.index)}",
  "currency_id": "${element(var.currencies_for_wallets, count.index)}"
}
EOF
}
