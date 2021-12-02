import os
import sys
from jinja2 import Environment, FileSystemLoader

def lambda_handler(event, context):
    env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates"), encoding="utf8"))
    template = env.get_template("home.html")
    html = template.render()
    return response(html)

def response(myhtml):
    return {
        "statusCode": 200,
        "body": myhtml,
        "headers": {
            "Content-Type": "text/html",
        }
    }

lambda_handler({}, {})