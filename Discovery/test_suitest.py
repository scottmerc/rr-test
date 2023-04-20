import os
import time
import json
from datetime import datetime

from apis.suitest_apis import SUITEST_API


class TestSuitest(object):

    api_token = os.getenv("HS_API_TOKEN")
    api = SUITEST_API(api_token)

    def test_suitest(self: "TestSuitest") -> None:
        next = self.api.devices()
        while True:
            if next == "done":
                break
            else:
                next = self.api.devices_follow(next)
