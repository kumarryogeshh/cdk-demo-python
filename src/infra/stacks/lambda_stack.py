from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
)
from constructs import Construct
from typing import Any, Dict, Optional

class LambdaStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.lambda_function = self.create_lambda_function()

    def create_lambda_function(self) -> _lambda.Function:
        return _lambda.Function(
            self,
            "HelloLambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="hello_lambda.handler",
            function_name="hello-lambda",
            code=_lambda.Code.from_asset("src/services/lambda"),
            environment={
                "ENV_VAR1": "value1",
                "ENV_VAR2": "value2"
            }
        )

    def add_environment_variable(self, key: str, value: str) -> None:
        if self.lambda_function.environment is None:
            self.lambda_function.environment = {}
        self.lambda_function.add_environment(key, value)

    def get_function_name(self) -> Optional[str]:
        return self.lambda_function.function_name

def main() -> None:
    from aws_cdk import App

    app = App()
    lambda_stack = LambdaStack(app, "HelloLambdaStack")
    
    # Example of adding an environment variable
    lambda_stack.add_environment_variable("NEW_VAR", "new_value")
    
    # Print the function name
    print(f"Lambda Function Name: {lambda_stack.get_function_name()}")
    
    app.synth()

if __name__ == "__main__":
    main()