import os
import sys
import json
import requests

def lambda_handler(myhevent, contexttml):
    return {
        "statusCode": 200,
        "body": "myhtml",
        "headers": {
            "Content-Type": "text/html",
        }
    }