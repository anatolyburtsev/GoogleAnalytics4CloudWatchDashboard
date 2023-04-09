from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_lambda_python_alpha as python,
    aws_secretsmanager as sm,
    DockerImage, Duration
)
from constructs import Construct


class AnalyticsLambdaStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Retrieve the GCP credentials secret
        gcp_credentials_secret = sm.Secret.from_secret_name_v2(self, "GCPCredentialsSecret", "hello_ga_secret_key")

        ga_lambda = _lambda.DockerImageFunction(
            self, "ga_hello_world",
            function_name="GA_hello_world",
            code=_lambda.DockerImageCode.from_image_asset(
                directory="./src"
            ),
            environment={},
            memory_size=512,
            timeout=Duration.seconds(900),
        )

        # Grant read permission for the secret to the Lambda function
        gcp_credentials_secret.grant_read(ga_lambda)
