import os
import sys
import json
import requests
from jinja2 import Environment, FileSystemLoader

def lambda_handler(event, context):
    # print(event)
    user_id = event["user_id"]
    recommended_events_url = "https://1ptsftnwde.execute-api.us-east-1.amazonaws.com/test/recommended_events"
    rec_resp = requests.get(recommended_events_url)
    recommended_events = json.loads(rec_resp.json()["body"])
    # print([event for event in recommended_events])
    data = {
        "upcoming_events": [],
        "recommended_events": recommended_events,
        "user_data": {
          "user_id":user_id
        }
    }
    env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates"), encoding="utf8"))
    template = env.get_template("home.html")
    html = template.render(
     data = data
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