variable "currencies" {
  description = "List of currencies"
  type = "list"
  default = ["btc","pasl","eth","zcl","altcom","ltc","arc","btg"]
}

resource "aws_cloudwatch_event_rule" "market_handler_event_rule" {
  count            = "${length(var.currencies)}"
  name                = "${var.app_name}_market_handler_event_rule_${element(var.currencies, count.index)}"
  description         = "Invoke ${element(aws_lambda_function.app_function.*.arn, 0)} every 5 mins"
  schedule_expression = "rate(5 minutes)"
}

resource "aws_lambda_permission" "market_handler_function_allow_cloud_watch" {
  count            = "${length(var.currencies)}"
  statement_id  = "AllowExecutionFromCloudWatch_${element(aws_cloudwatch_event_rule.market_handler_event_rule.*.name, count.index)}"
  action        = "lambda:InvokeFunction"
  function_name = "${element(aws_lambda_function.app_function.*.arn, 0)}"
  principal     = "events.amazonaws.com"
  source_arn    = "${element(aws_cloudwatch_event_rule.market_handler_event_rule.*.arn, count.index)}"
}

resource "aws_cloudwatch_event_target" "currency" {
  count            = "${length(var.currencies)}"
  rule  = "${element(aws_cloudwatch_event_rule.market_handler_event_rule.*.id, count.index)}"
  arn  = "${element(aws_lambda_function.app_function.*.arn, 0)}"
  input =  <<EOF
{"currency_id": "${element(var.currencies, count.index)}"}
EOF
}
