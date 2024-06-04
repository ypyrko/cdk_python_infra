from aws_cdk import (
    Stack,
    aws_dynamodb,
    aws_lambda,
    aws_apigateway,

)
from constructs import Construct
import os

class CdkPythonInfraStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # DynamoDB for Lambda to store the information (for example about users)    
        user_info_table = aws_dynamodb.Table(
            self, 
            id='dynamoTable', 
            table_name='UserInfo', 
            partition_key=aws_dynamodb.Attribute(
                name='userid', 
                type=aws_dynamodb.AttributeType.STRING
            )
        )

        # Lambda function to handle API requests
        request_handler_lambda = aws_lambda.Function(
            self, 
            id='lambdafunction', 
            function_name="formlambda", 
            runtime=aws_lambda.Runtime.PYTHON_3_12,
            handler='index.handler',
            code=aws_lambda.Code.from_asset(
                os.path.join("./", "lambda-handler")),
            environment={
                # 'bucket': my_bucket.bucket_name,
                'table': user_info_table.table_name
            }
        )

        # Grant Lamda function read and write permissions to the DB
        user_info_table.grant_read_write_data(request_handler_lambda)

        # APIGateway 
        api_gateway = aws_apigateway.LambdaRestApi(
            self, 
            id='lambdaapi', 
            rest_api_name='formapi', 
            handler=request_handler_lambda, 
            proxy=True
        )
