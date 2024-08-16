import aws_cdk as core
import aws_cdk.assertions as assertions
from src.infra.stacks.lambda_stack import LambdaStack

def test_lambda_function_created():
    app = core.App()
    stack = LambdaStack(app, "MyTestStack")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::Lambda::Function", {
        "Runtime": "python3.11",
        "Handler": "hello_lambda.handler"
    })

def test_lambda_function_env_vars():
    app = core.App()
    stack = LambdaStack(app, "MyTestStack")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::Lambda::Function", {
        "Environment": {
            "Variables": {
                "ENV_VAR1": "value1",
                "ENV_VAR2": "value2"
            }
        }
    })