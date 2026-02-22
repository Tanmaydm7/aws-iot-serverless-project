AWS IoT Serverless Monitoring Project
Architecture

AWS IoT Core – Receives sensor data using MQTT protocol

AWS Lambda – Processes incoming IoT data

Amazon DynamoDB – Stores device data

Amazon CloudWatch – Monitors DynamoDB metrics

Amazon SNS – Sends alert notifications

Flow

IoT device publishes sensor data using MQTT

AWS IoT Rule triggers a Lambda function

Lambda validates and stores data in DynamoDB

CloudWatch monitors DynamoDB write capacity

SNS sends alert when threshold is breached

Deployment Steps
1. Create DynamoDB Table

Partition Key: deviceId

Sort Key: timestamp

2. Create IAM Role

Grant access to:

DynamoDB

CloudWatch Logs

SNS

3. Deploy Lambda Function

Runtime: Python 3.x

Attach IAM role

Upload Lambda code

4. Configure AWS IoT Rule

Define SQL query for incoming MQTT messages

Set Lambda as rule action

5. Create CloudWatch Alarm

Metric: ConsumedWriteCapacityUnits

Threshold: Greater than defined limit

Action: Trigger SNS notification

Security

AWS credentials are not stored in the repository

Sensitive files are excluded using .gitignore

IAM policies follow least privilege principle


Purpose

This project is created for educational and learning purposes to understand AWS serverless IoT architecture.
