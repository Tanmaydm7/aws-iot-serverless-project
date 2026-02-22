import json

def lambda_handler(event, context):
    print("CloudWatch Alarm Triggered")
    print(json.dumps(event))

    return {
        'statusCode': 200,
        'body': 'Alarm notification processed'
    }
