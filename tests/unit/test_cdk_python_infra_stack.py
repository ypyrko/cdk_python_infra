import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_python_infra.cdk_python_infra_stack import CdkPythonInfraStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_python_infra/cdk_python_infra_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkPythonInfraStack(app, "cdk-python-infra")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
