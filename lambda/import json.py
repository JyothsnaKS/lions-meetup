import json
import boto3

def get_event_details(event_ids):
    sts_connection = boto3.client('sts')
    acct_b = sts_connection.assume_role(
        RoleArn="arn:aws:iam::283759418474:role/LionsDynamoRole",
        RoleSessionName="cross_acct_lambda"
    )
    
    ACCESS_KEY = acct_b['Credentials']['AccessKeyId']
    SECRET_KEY = acct_b['Credentials']['SecretAccessKey']
    SESSION_TOKEN = acct_b['Credentials']['SessionToken']
    
    client = boto3.client(
        'dynamodb',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        aws_session_token=SESSION_TOKEN,
    )
    data = client.batch_get_item(RequestItems={'event_details':{'Keys':[{'item_id': {'N': event_ids[0]}}, {'item_id': {'N': event_ids[1]}}, {'item_id': {'N': event_ids[2]}},{'item_id': {'N': event_ids[3]}},{'item_id': {'N': event_ids[4]}},{'item_id': {'N': event_ids[5]}},{'item_id': {'N': event_ids[6]}},{'item_id': {'N': event_ids[7]}},{'item_id': {'N': event_ids[8]}},{'item_id': {'N': event_ids[9]}}]}})
    print(data)

    events = data['Responses']['event_details']
    results = list()
    for event in events:
        result = dict()
        result['item_id'] = event['item_id']['N']
        result['name_text'] = event['name_text']['S']
        result['category'] = event['category']['S']
        result['online_event'] = event['online_event']['BOOL']
        result['start_local'] = event['start_local']['S']
        result['end_local'] = event['end_local']['S']
        results.append(result)
    print(results)
    return results
    
def lambda_handler(event, context):
    sts_connection = boto3.client('sts')
    acct_b = sts_connection.assume_role(
        RoleArn="arn:aws:iam::917162228091:role/aws-personalize-lambda",
        RoleSessionName="cross_acct_lambda"
    )
    
    ACCESS_KEY = acct_b['Credentials']['AccessKeyId']
    SECRET_KEY = acct_b['Credentials']['SecretAccessKey']
    SESSION_TOKEN = acct_b['Credentials']['SessionToken']
    
    personalizeRt = boto3.client(
        'personalize-runtime',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        aws_session_token=SESSION_TOKEN,
    )

    response = personalizeRt.get_recommendations( campaignArn = 'arn:aws:personalize:us-east-1:917162228091:campaign/events-prediction-campaign',
    userId = '1',
    numResults = 10
    )
    event_ids = list()
    for item in response['itemList']:
        event_ids.append(item['itemId'])
        
    results = get_event_details(event_ids)

    return {
        'statusCode': 200,
        'body': json.dumps(results)
    }
