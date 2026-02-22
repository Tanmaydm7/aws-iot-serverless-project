import json
import boto3
from datetime import datetime

dynamodb = boto3.client('dynamodb')
TABLE_NAME = "IoTDeviceData"

def lambda_handler(event, context):
    try:
        payload = json.loads(event['Records'][0]['Sns']['Message']) if 'Records' in event else event

        response = dynamodb.put_item(
            TableName=TABLE_NAME,
            Item={
                'deviceId': {'S': payload['deviceId']},
                'timestamp': {'S': datetime.utcnow().isoformat()},
                'temperature': {'N': str(payload['temperature'])},
                'humidity': {'N': str(payload['humidity'])}
            }
        )

        return {
            'statusCode': 200,
            'body': 'Data stored successfully'
        }

    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': 'Error processing data'
        }
