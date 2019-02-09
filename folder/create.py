import json
import logging
import os
import time
import uuid

import boto3
dynamodb = boto3.resource('dynamodb')


def create(event, context):
    data = json.loads(event['body'])
    if 'name' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the folder - no name provided.")
        return

    timestamp = int(time.time() * 1000)

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    folder = {
        'id': str(uuid.uuid1()),
        'name': data['name'],
        'createdAt': timestamp,
        'updatedAt': timestamp,
    }

    table.put_item(Item=folder)

    return {
        "statusCode": 200,
        "body": json.dumps(folder)
    }
