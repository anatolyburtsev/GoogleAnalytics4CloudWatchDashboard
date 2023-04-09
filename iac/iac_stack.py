from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct

from iac.analytics_lambda_stack import AnalyticsLambdaStack


class IacStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_stack = AnalyticsLambdaStack(self, "analytics_lambda_stack")
