# Setup an event to trigger the lambafunction
resource "aws_cloudwatch_event_rule" "profitability_handler_event_rule" {
  name                = "${var.app_name}_profitability_handler_event_rule"
  description         = "Invoke ${element(aws_lambda_function.app_function.*.arn, 1)} every 2 mins"
  schedule_expression = "rate(2 minutes)"
}

resource "aws_lambda_permission" "profitability_handler_function_allow_cloud_watch" {
  statement_id  = "AllowExecutionFromCloudWatch"
  action        = "lambda:InvokeFunction"
  function_name = "${element(aws_lambda_function.app_function.*.arn, 1)}"
  principal     = "events.amazonaws.com"
  source_arn    = "${aws_cloudwatch_event_rule.profitability_handler_event_rule.arn}"
}

# Setup the targets for this event:
resource "aws_cloudwatch_event_target" "all" {
  rule  = "${aws_cloudwatch_event_rule.profitability_handler_event_rule.id}"
  arn  = "${element(aws_lambda_function.app_function.*.arn, 1)}"
}
