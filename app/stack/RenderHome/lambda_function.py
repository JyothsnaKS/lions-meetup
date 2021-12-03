import os
import sys
import json
from jinja2 import Environment, FileSystemLoader

def lambda_handler(event, context):
    soc_events = [{
  "item_id": {
    "N": "169178059129"
  },
  "category_id": {
    "N": "110"
  },
  "format_id": {
    "N": "11"
  },
  "start_utc": {
    "S": "2021-09-02T02:00:00Z"
  },
  "published": {
    "S": "2021-08-31T20:37:34Z"
  },
  "end_utc": {
    "S": "2023-02-02T12:00:00Z"
  },
  "is_externally_ticketed": {
    "BOOL": True
  },
  "start_local": {
    "S": "2021-09-01T22:00:00"
  },
  "organizer_id": {
    "N": "22604456275"
  },
  "name_text": {
    "S": "Perreo Island Wednesday at Acapulco Night Club"
  },
  "venue_id": {
    "N": "63065547"
  },
  "is_locked": {
    "BOOL": True
  },
  "is_series_parent": {
    "BOOL": True
  },
  "start_timezone": {
    "S": "America/New_York"
  },
  "shareable": {
    "BOOL": True
  },
  "inventory_type": {
    "S": "limited"
  },
  "end_local": {
    "S": "2023-02-02T07:00:00"
  },
  "summary": {
    "S": "The Hottest Latin Party To Hit Queens On a Wednesday Night!"
  },
  "organization_id": {
    "N": "310770345525"
  },
  "locale": {
    "S": "en_US"
  },
  "source": {
    "S": "coyote"
  },
  "tx_time_limit": {
    "N": "480"
  },
  "privacy_setting": {
    "S": "unlocked"
  },
  "subcategory_id": {
    "N": "10999"
  },
  "description_text": {
    "S": "The Hottest Latin Party To Hit Queens On a Wednesday Night!"
  },
  "is_reserved_seating": {
    "BOOL": True
  },
  "is_free": {
    "BOOL": True
  },
  "category": {
    "S": "food-and-drink"
  },
  "online_event": {
    "BOOL": True
  },
  "facebook_event_id": {
    "N": "0"
  },
  "is_series": {
    "BOOL": True
  }
}]
    data = {
        "upcoming_events": soc_events
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