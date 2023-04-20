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
from tabulate import tabulate


class SUITEST_API:
    def __init__(self, api_token):
        self.api_token = api_token
        self.url_root = "https://the.suite.st/api/public/v4/"
        self.headers = {}
        self.headers["Authorization"] = "Basic {}".format(api_token)
        self.headers["accept"] = "application/json"
        self.webhook = os.getenv("WEBHOOK")

    def devices(self, table):
        request_url = self.url_root + "/devices?limit=100"
        r = requests.get(request_url, headers=self.headers)
        response = json.loads(r.text)
        values = response["values"]
        for items in values:
            if "HS-" in items["customName"]:
                if (
                    items["status"] != "READY"
                    and items["status"] != "CONTROLLABLE"
                    and items["status"] != "API_CONTROLLED"
                ):
                    temp = [items["customName"], items["status"], items["ipAddress"]]
                    table.append(temp)
        return response["next"], table

    def devices_follow(self, url, table):
        request_url = url
        r = requests.get(request_url, headers=self.headers)
        response = json.loads(r.text)
        values = response["values"]
        for items in values:
            if "HS-" in items["customName"]:
                if (
                    items["status"] != "READY"
                    and items["status"] != "CONTROLLABLE"
                    and items["status"] != "API_CONTROLLED"
                ):
                    temp = [items["customName"], items["status"], items["ipAddress"]]
                    table.append(temp)
        if "next" in response.keys():
            return response["next"], table
        else:
            return "done", table

    def alert_slack(self, text):
        request_url = self.webhook
        payload = {"text": "```{}```".format(text)}
        payload = json.dumps(payload)
        response = requests.post(
            request_url,
            data=payload,
        )
        print(response)
