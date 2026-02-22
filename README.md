AWS IoT Serverless Monitoring Project
📌 Project Overview

This project demonstrates a serverless IoT data monitoring system built using AWS cloud services.
IoT devices publish sensor data to AWS IoT Core, which is processed using AWS Lambda and stored in DynamoDB.
CloudWatch monitors system metrics and triggers alerts using SNS when thresholds are exceeded.

🏗️ Architecture

Services Used:

AWS IoT Core – Device communication (MQTT)

AWS Lambda – Serverless data processing

Amazon DynamoDB – NoSQL data storage

Amazon CloudWatch – Monitoring & alarms

Amazon SNS – Notifications

High-Level Flow:

IoT device publishes sensor data via MQTT

AWS IoT Rule triggers a Lambda function

Lambda validates and stores data in DynamoDB

CloudWatch monitors DynamoDB write capacity

SNS sends alerts when thresholds are breached

📁 Project Structure
aws-iot-project/
│
├── lambda/
│   ├── data_ingest.py
│   └── alert_handler.py
│
├── iot/
│   ├── device_publish.py
│   └── mqtt_config.json
│
├── dynamodb/
│   └── table_schema.json
│
├── cloudwatch/
│   └── write_capacity_alarm.json
│
├── iam/
│   └── lambda_policy.json
│
├── .gitignore
├── README.md
└── requirements.txt
⚙️ Setup & Deployment Steps
1️⃣ Create DynamoDB Table

Partition Key: deviceId

Sort Key: timestamp

2️⃣ Create IAM Role

Allow access to:

DynamoDB

CloudWatch Logs

SNS

3️⃣ Deploy Lambda Function

Runtime: Python 3.x

Attach IAM role

Upload code from /lambda

4️⃣ Configure AWS IoT

Create an IoT Thing

Attach certificate & policy

Create IoT Rule to trigger Lambda

5️⃣ Setup CloudWatch Alarm

Metric: ConsumedWriteCapacityUnits

Threshold: > 1

Action: Trigger SNS notification

📊 Sample DynamoDB Item
{
  "deviceId": { "S": "sensor01" },
  "temperature": { "N": "29" },
  "humidity": { "N": "60" },
  "timestamp": { "S": "2026-02-22T18:40:00" }
}
🔔 Monitoring & Alerts

CloudWatch continuously monitors DynamoDB metrics

When write capacity crosses the defined threshold:

Alarm state changes to IN ALARM

SNS sends notification to subscribed email

🔐 Security Best Practices

AWS credentials are not stored in the repository

.gitignore excludes:

.env

.aws/

*.pem

IAM follows least privilege principle

🧪 Testing

Publish test data using IoT device script

Verify data insertion in DynamoDB

Force higher write throughput to test CloudWatch alarms

Confirm SNS notification delivery

🎯 Use Cases

IoT sensor monitoring

Smart environment tracking

Serverless data ingestion pipelines

Cloud monitoring and alerting systems

📚 Learning Outcomes

Hands-on experience with AWS serverless architecture

Understanding IoT data pipelines

CloudWatch monitoring and alert configuration

Secure cloud project version control using GitHub

AWS IoT & Serverless Cloud Project

📝 License

This project is for educational and learning purposes.
