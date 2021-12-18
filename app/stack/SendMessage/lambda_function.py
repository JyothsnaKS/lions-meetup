import os
import sys
import json
import requests
import boto3

def send_to_connection(connection_id, data):
    gatewayapi = boto3.client("apigatewaymanagementapi",
            endpoint_url = "https://1fgoc12ik5.execute-api.us-east-1.amazonaws.com/production")
    return gatewayapi.post_to_connection(ConnectionId=connection_id,
            Data=json.dumps(data).encode('utf-8'))

def fetch_all_event_connections(event_id):
    try:
        client = boto3.resource('dynamodb', endpoint_url="https://dynamodb.us-east-1.amazonaws.com")
        table = client.Table('connections')
        response = table.query(
            KeyConditionExpression="event_id = :event_id",
            ExpressionAttributeValues={":event_id": event_id},
        )
        items = response.get("Items", [])
        return items
    except Exception as error:
        print("Error when storing in DB %s" % error)

def save_to_chat_history(data):
    try:
        client = boto3.resource('dynamodb', endpoint_url="https://dynamodb.us-east-1.amazonaws.com")
        table = client.Table('chat-history')
        table.put_item(
            Item=data
        )
    except Exception as error:
        print("Error when storing in DB %s" % error)

def send_message(data):
    connections = fetch_all_event_connections(data["event_id"])
    for connection in connections:
        send_to_connection(connection["connection_id"], data)
    save_to_chat_history(data)
    
def lambda_handler(myevent, context):
    for record in myevent["Records"]:
        data = dict()
        deserializer = boto3.dynamodb.types.TypeDeserializer()
        new_record = {k: deserializer.deserialize(v) for k,v in record["NewImage"].items()}
        send_message(new_record)
        send_message(data)
    return {
        "statusCode": 200,
        "body": "myhtml",
        "headers": {
            "Content-Type": "text/html",
        }
    }