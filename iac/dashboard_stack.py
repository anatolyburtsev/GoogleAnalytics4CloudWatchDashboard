from aws_cdk import (
    Stack,
    aws_cloudwatch as cloudwatch,
    aws_lambda as _lambda
)
from constructs import Construct


class DashboardStack(Stack):
    def __init__(self, scope: Construct, id: str, ga_lambda: _lambda.Function, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create a CloudWatch Dashboard
        dashboard = cloudwatch.Dashboard(self, "GADemoWidget",
                                         dashboard_name="GAHelloWidget")

        # Add widgets to the dashboard
        dashboard.add_widgets(
            cloudwatch.TextWidget(markdown="# Welcome to the GA HelloWorld Dashboard", width=24),
            cloudwatch.CustomWidget(
                function_arn=ga_lambda.function_arn,
                title="GA HelloWorld",
                width=8
            )
        )

