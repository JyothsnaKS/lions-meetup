import boto3

def store_db(data):
    try:
        client = boto3.resource('dynamodb', endpoint_url="https://dynamodb.us-east-1.amazonaws.com")
        table = client.Table('live-chat')
        table.put_item(
            Item=data
        )
    except Exception as error:
        print("Error when storing in DB %s" % error)


def lambda_handler(myevent, context):
    print(myevent)
    data = dict()
    connectionID = myevent["requestContext"].get("connectionId")
    # userId = myevent["requestContext"].get("connectionId")
    return {
        "statusCode": 200,
        "body": "myhtml",
        "headers": {
            "Content-Type": "text/html",
        }
    }