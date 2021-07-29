import boto3
import os
import json
from http import HTTPStatus

DONUTS_TABLE = os.environ.get("DONUTS_TABLE_NAME")


def get_handler(event, context):
    dynamodb = boto3.resource("dynamodb").Table(DONUTS_TABLE)
    donuts = dynamodb.scan().get("Items", [])

    return {
        "statusCode": HTTPStatus.OK,
        "body": json.dumps(donuts)
    }
