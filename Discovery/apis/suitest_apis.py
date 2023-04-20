import requests
import json
import traceback
import logging
import datetime
import pytest
import time
import calendar
import os
from datetime import timedelta


class SUITEST_API:
    def __init__(self, api_token):
        self.api_token = api_token
        self.url_root = "https://the.suite.st/api/public/v4/"
        self.headers = {}
        self.headers["Authorization"] = "Basic {}".format(api_token)
        self.headers["accept"] = "application/json"
        self.webhook = os.getenv("WEBHOOK")

    def devices(self):
        request_url = self.url_root + "/devices?limit=100"
        r = requests.get(request_url, headers=self.headers)
        response = json.loads(r.text)
        values = response["values"]
        for items in values:
            if "HS-" in items["customName"]:
                if items["status"] != "READY" and items["status"] != "CONTROLLABLE":
                    print(
                        "Device Name: {} Status: {} IP: {}".format(
                            items["customName"], items["status"], items["ipAddress"]
                        )
                    )
                    ## Send Slack Message
                    self.alert_slack(
                        items["customName"], items["status"], items["ipAddress"]
                    )
        return response["next"]

    def devices_follow(self, url):
        request_url = url
        r = requests.get(request_url, headers=self.headers)
        response = json.loads(r.text)
        values = response["values"]
        for items in values:
            if "HS-" in items["customName"]:
                if items["status"] != "READY" and items["status"] != "CONTROLLABLE":
                    print(
                        "Device Name: {} Status: {} IP: {}".format(
                            items["customName"], items["status"], items["ipAddress"]
                        )
                    )
                    ### Send Slack Message
                    self.alert_slack(
                        items["customName"], items["status"], items["ipAddress"]
                    )
        if "next" in response.keys():
            return response["next"]
        else:
            return "done"

    def alert_slack(self, name, status, ip):
        request_url = self.webhook
        payload = {
            "blocks": [
                {"type": "divider"},
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": "🚨Suitest Device Offline🚨"},
                },
                {
                    "type": "section",
                    "fields": [
                        {"type": "mrkdwn", "text": "*Device Name:*\n{}".format(name)},
                        {"type": "mrkdwn", "text": "*Status:*\n{}".format(status)},
                        {"type": "mrkdwn", "text": "*IP Address:*\n{}".format(ip)},
                    ],
                },
                {"type": "divider"},
            ]
        }
        payload = json.dumps(payload)
        response = requests.post(
            request_url,
            data=payload,
        )
        print(response)
