import json
import requests
import os

def lambda_handler(event, context):
    payload = {
        "subnet_id": os.environ['SUBNET_ID'],
        "name": "chetan badgujar",
        "email": "badgujarchetan80@gmail.com"
    }

    url = "https://bc1yy8dzsg.execute-api.eu-west-1.amazonaws.com/v1/data"
    headers = {'X-Siemens-Auth': 'test'}

    response = requests.post(url, headers=headers, json=payload)
    
    return {
        'statusCode': response.status_code,
        'body': response.json()
    }

