import json
import time
import logging
import os

from shared import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


def update(event, context):
    data = json.loads(event['body'])
    if 'name' not in data:
        raise Exception("Couldn't update the bookmark item.")
        return

    timestamp = int(time.time() * 1000)

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    result = table.update_item(
        Key={
            'id': event['pathParameters']['id']
        },
        ExpressionAttributeNames={
          '#folder_name': 'name',
        },
        ExpressionAttributeValues={
          ':name': data['name'],
          ':updatedAt': timestamp,
        },
        UpdateExpression='SET #folder_name = :name, '
                         'updatedAt = :updatedAt',
        ReturnValues='ALL_NEW',
    )

    return {
        "statusCode": 200,
        "body": json.dumps(result['Attributes'],
                           cls=decimalencoder.DecimalEncoder)
    }
