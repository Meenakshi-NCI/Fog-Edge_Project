import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('SmartChairData')

def lambda_handler(event, context):
    for record in event['Records']:
        data = json.loads(record['body'])

        table.put_item(
            Item=data
        )

    return {"status": "stored"}