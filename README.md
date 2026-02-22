# AWS IoT Serverless Monitoring Project

## Architecture
- AWS IoT Core
- AWS Lambda
- DynamoDB
- CloudWatch Alarms
- SNS Notifications

## Flow
1. IoT device publishes MQTT data
2. Lambda processes and stores data in DynamoDB
3. CloudWatch monitors write capacity
4. SNS sends alert on threshold breach

## Deployment Steps
1. Create DynamoDB table
2. Create IAM role
3. Deploy Lambda function
4. Configure IoT rule
5. Create CloudWatch alarm
