import json
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.utilities.data_classes import event_source, ALBEvent

@event_source(data_class=ALBEvent)
def hello(event: ALBEvent, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
