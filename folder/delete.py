import os

import boto3
dynamodb = boto3.resource('dynamodb')


def delete(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # delete the folder from the database
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )
    if result.get('Item', None):
        table.delete_item(
            Key={
                'id': result['Item']['id'],
            }
        )
        return {
            "statusCode": 200,
        }

    return {
        "statusCode": 400,
    }