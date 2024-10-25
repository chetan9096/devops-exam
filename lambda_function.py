import os
import json
import requests
import base64

def lambda_handler(event, context):
    try:
        if 'SUBNET_ID' not in os.environ:
            raise ValueError("Environment variable 'SUBNET_ID' is not set.")
        
        subnet_id = os.environ['SUBNET_ID']
        print(f"Subnet ID: {subnet_id}") 
        
        payload = {
            "subnet_id": subnet_id,
            "name": "Chetan Badgujar",
            "email": "badgujarchetan80@gmail.com"
        }
        print(f"Payload: {json.dumps(payload)}")  
        
        response = requests.post(
            "https://bc1yy8dzsg.execute-api.eu-west-1.amazonaws.com/v1/data",
            headers={'X-Siemens-Auth': 'test'},
            json=payload
        )
        
        response.raise_for_status()  
        
        print(f"API Response: {response.json()}")
        
        log_result = response.headers.get("X-Amzn-Trace-Id")  

        # Decode the log_result 
        decoded_log_result = base64.b64decode(log_result).decode('utf-8')
        print(f"Decoded Log Result: {decoded_log_result}")

        return {
            "statusCode": 200,
            "body": json.dumps(response.json())
        }
    
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Request failed", "details": str(e)})
        }
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "An unexpected error occurred", "details": str(e)})
        }
