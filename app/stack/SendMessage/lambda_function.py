import os
import sys
import json
import requests
import boto3

def _send_to_connection(connection_id, data, event):
    gatewayapi = boto3.client("apigatewaymanagementapi",
            endpoint_url = "https://" + event["requestContext"]["domainName"] +
                    "/" + event["requestContext"]["stage"])
    return gatewayapi.post_to_connection(ConnectionId=connection_id,
            Data=json.dumps(data).encode('utf-8'))
            
def lambda_handler(myevent, context):
    print(myevent)
    data = {"messages": ["hello from lambda"]}
    connectionID = myevent["requestContext"].get("connectionId")
    _send_to_connection(connectionID, data, myevent)
    return {
        "statusCode": 200,
        "body": "myhtml",
        "headers": {
            "Content-Type": "text/html",
        }
    }