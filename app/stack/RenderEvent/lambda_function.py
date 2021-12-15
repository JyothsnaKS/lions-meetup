import os
import json
import requests
from jinja2 import Environment, FileSystemLoader

def lambda_handler(event, context):
    # print(event)
    user_id = event["user_id"]
    event_id = event["event_id"]
    event_details_url = "https://1ptsftnwde.execute-api.us-east-1.amazonaws.com/test/get_event_details?event_id=" + str(event_id)
    rec_resp = requests.get(event_details_url)
    print(rec_resp.json())
    res_json = rec_resp.json()
    not_found = False
    if res_json["statusCode"] != 200:
        not_found = True
    event_details = res_json["body"]
    # print([event for event in recommended_events])
    data = {
        "user_data": {
          "user_id" : user_id
        }
    }
    joined_events_url = "https://1ptsftnwde.execute-api.us-east-1.amazonaws.com/test/display_my_events"
    joined_rec_resp = requests.get(joined_events_url)
    joined_resp_json = joined_rec_resp.json()
    joined_events = []
    if "body" in joined_resp_json:
        joined_events = json.loads(joined_rec_resp.json()["body"])
        
    env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates"), encoding="utf8"))
    template = env.get_template("event.html")
    html = template.render(
     data = data,
     event = event_details,
     not_found = not_found
    )
    return response(html)

def response(myhtml):
    return {
        "statusCode": 200,
        "body": myhtml,
        "headers": {
            "Content-Type": "text/html",
        }
    }