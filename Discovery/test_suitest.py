import os
import time
import json
from datetime import datetime
from apis.suitest_apis import SUITEST_API
from tabulate import tabulate


class TestSuitest(object):

    api_token = os.getenv("HS_API_TOKEN")
    api = SUITEST_API(api_token)
    slack_token = os.getenv("SLACK")
    channel = "wbd-suitest-alerts"
    table = []

    def test_suitest(self: "TestSuitest") -> None:

        next, self.table = self.api.devices(self.table)
        while True:
            if next == "done":
                break
            else:
                next, self.table = self.api.devices_follow(next, self.table)

        print("/n")
        print(tabulate(self.table, headers=["Device Name", "Status", "IP"]))
        self.api.alert_slack(
            tabulate(self.table, headers=["Device Name", "Status", "IP"])
        )
