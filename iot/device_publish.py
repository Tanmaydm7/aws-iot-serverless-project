import json
import time
import random
import paho.mqtt.client as mqtt

BROKER = "your-endpoint.iot.region.amazonaws.com"
TOPIC = "iot/sensor/data"

client = mqtt.Client()
client.connect(BROKER, 8883)

while True:
    data = {
        "deviceId": "sensor01",
        "temperature": random.randint(20, 40),
        "humidity": random.randint(40, 80)
    }

    client.publish(TOPIC, json.dumps(data))
    print("Published:", data)

    time.sleep(5)
