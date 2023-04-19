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

from apis.hs_logger import logger, setup_logger


class HS_API:

    start_time = 0
    end_time = 0

    # INTIALIZATION OF APIs WITH HS API TOKEN
    def __init__(self, api_token, device_address=None):
        self.api_token = api_token
        self.url_root = "https://api-dev.headspin.io/v0/"
        self.headers = {}
        self.headers["Authorization"] = "Bearer {}".format(api_token)
        self.device_address = device_address
        self.webhook = os.getenv("WEBHOOK")
        self.host = os.getenv("HOSTNAME")

    def alert_slack_success(self, session_id, type):
        request_url = self.webhook
        payload = {
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "✅ {} Test Case Passed:\nHost:{}\nSession URL: *<https://ui.headspin.io/sessions/{}/waterfall>*".format(
                            type, self.host, session_id
                        ),
                    },
                },
            ]
        }
        payload = json.dumps(payload)
        response = requests.post(
            request_url,
            data=payload,
        )
        print(response)

    def alert_slack_failure(self, session_id, type, exceptions):
        request_url = self.webhook
        payload = {
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "⛔️ {} Test Case Failed:\nHost: {}\nSession URL: *<https://ui.headspin.io/sessions/{}/waterfall>*\n{}".format(
                            type, self.host, session_id, exceptions
                        ),
                    },
                },
            ]
        }
        payload = json.dumps(payload)
        response = requests.post(
            request_url,
            data=payload,
        )
        print(response)

    def upload_image(self, imageBase64):
        url_root = "https://api.upload.io/v2/accounts/kW15bF8/uploads/binary"
        headers = {}
        headers["Authorization"] = "Bearer public_kW15bF87pxTCRRopZXSRKiFsCCmi"
        payload = imageBase64
        response = requests.post(url_root, headers=headers, data=payload)
        if response.status_code == 200:
            print(response)

    # START A PERFORMANCE SESSION PROGRAMATICALLY
    def start_session(self, device_address):
        request_url = self.url_root + "sessions"
        payload = {}
        payload["session_type"] = "capture"
        payload["device_address"] = device_address
        payload["allow_replace"] = True
        payload["capture_video"] = True
        payload["capture_network"] = False
        payload = json.dumps(payload)
        print("Starting Capture....\n")
        response = requests.post(
            request_url, headers=self.headers, data=payload, verify=False
        )
        # print(response.text.encode('utf8'))
        json_data = json.loads(response.text)
        if response.status_code == 200:
            return json_data["session_id"]
        else:
            print("Error starting capture....\n")
            pytest.raises(Exception)

    def reliability(self, hostname, status, device_id, message, session_id=None):
        request_url = self.url_root + "reliability/report-status"
        payload = {}
        if session_id != None:
            payload["session_id"] = session_id
        payload["hostname"] = hostname
        payload["status"] = status
        payload["device_id"] = device_id
        payload["message"] = message
        payload = json.dumps(payload)
        response = requests.post(
            request_url, headers=self.headers, data=payload, verify=False
        )
        print(response)

    # STOP A PERFORMANCE SESSION PROGRAMATICALLY
    def stop_session(self, session_id):
        request_url = self.url_root + "sessions/{}".format(session_id)
        payload = '{"active": false}'
        response = requests.patch(
            request_url, headers=self.headers, data=payload, verify=False
        )
        # print(response.text.encode('utf8'))
        json_data = json.loads(response.text)
        if response.status_code == 200:
            print("Stopped session capture.... {}\n".format(json_data["msg"]))
        else:
            print("Error stopping capture....\n")

    def get_android_device(self, device_id):
        logger.info("Grabbing Android Manufacturer")
        request_url = self.url_root + "adb/devices"
        r = requests.get(request_url, headers=self.headers, verify=False)
        response = json.loads(r.text)
        for host in response.keys():
            if device_id in host:
                return response[host].get("model")

    def get_automation_config(self, device_id):
        print("\n")
        logger.info("Grabbing Automation Config")
        request_url = self.url_root + "devices/automation-config"
        r = requests.get(request_url, headers=self.headers, verify=False)
        response = json.loads(r.text)
        for host in response.keys():
            if device_id in host:
                return (
                    response[host].get("capabilities"),
                    response[host].get("driver_url"),
                )
        return None

    def upload_results(self, session_id, test_name=None):
        request_url = self.url_root + "perftests/upload"
        payload = {}
        payload["session_id"] = session_id
        payload["status"] = "passed"
        if test_name != None:
            payload["test_name"] = test_name
        payload = json.dumps(payload)
        response = requests.post(
            request_url, headers=self.headers, data=payload, verify=False
        )
        if response.status_code == 200:
            logger.info("Test Uploaded to Userflow")
        else:
            logger.error("Test could not be uploaded: {}".format(response.text))

    def add_tags(self, session_id, tags):
        request_url = self.url_root + "sessions/tags/{}".format(session_id)
        payload = json.dumps(tags)
        logger.info(payload)
        response = requests.post(
            request_url, headers=self.headers, data=payload, verify=False
        )
        if response.status_code == 200:
            logger.info("Tags Applied")
        else:
            logger.error("Tags could not be applied: {}".format(response.text))

    def adb_shell(self, device_id, command):
        request_url = self.url_root + "adb/{}/shell".format(device_id)
        payload = command
        response = requests.post(
            request_url, headers=self.headers, data=payload, verify=False
        )
        r = json.loads(response.text)
        if response.status_code == 200:
            return r["stdout"]
        else:
            logger.error("Could not retrieve adb info")

    def device_info(self, device_id):
        request_url = self.url_root + "devices"
        response = requests.get(request_url, headers=self.headers, verify=False)
        r = json.loads(response.text)
        if response.status_code == 200:
            entries = r["devices"]
            for i in entries:
                if i["serial"] == device_id:
                    return (i["operator"], i["carriers"])
        else:
            logger.error("Could not device info")

    def page_load(self, session_id, ts_start, ts_end, name, sensitivy=False):
        request_url = self.url_root + "sessions/analysis/pageloadtime/{}".format(
            session_id
        )
        payload = {}
        region_times = []
        start_end = {}
        start_end["name"] = name
        start_end["ts_start"] = ts_start
        start_end["ts_end"] = ts_end
        if sensitivy == True:
            start_end["start_sensitivity"] = 0.835
            start_end["end_sensitivity"] = 0.835
        region_times.append(start_end)
        payload["regions"] = region_times
        payload = json.dumps(payload)
        response = requests.post(
            request_url, headers=self.headers, data=payload, verify=False
        )
        if response.status_code == 200:
            logger.info("Vsisual page load analysis")
        else:
            logger.error("VPLA could not be calculated")

    def name_session(self, session_id, name, desc=None):
        request_url = self.url_root + "sessions/{}/description".format(session_id)
        payload = {}
        payload["name"] = name
        payload["description"] = name
        payload = json.dumps(payload)
        response = requests.post(request_url, headers=self.headers, data=payload)
        if response.status_code == 200:
            logger.info("Name/Description Added")
        else:
            logger.error("Test could not be named: {}".format(response.text))

    def upload_results(self, session_id, status, userflow_id, test_name=None):
        request_url = self.url_root + "userflows/{}/sessions".format(userflow_id)
        payload = {}
        payload["session_id"] = session_id
        payload["status"] = status
        if test_name != None:
            payload["test_name"] = test_name
        payload = json.dumps(payload)
        response = requests.post(request_url, headers=self.headers, data=payload)
        if response.status_code == 200:
            logger.info("Test Uploaded to Userflow")
        else:
            logger.error("Test could not be uploaded: {}".format(response.text))

    def lock_device(self, device_id):
        request_url = self.url_root + "adb/{}/lock".format(device_id)
        response = requests.post(request_url, headers=self.headers)
        r = json.loads(response.text)
        if response.status_code == 200:
            logger.info("Locking {}".format(device_id))
            return True
        else:
            logger.error("Could not lock device")
            raise Exception("Could not lock {}".format(device_id))

    def unlock_device(self, device_id):
        request_url = self.url_root + "adb/{}/unlock".format(device_id)
        response = requests.post(request_url, headers=self.headers)
        r = json.loads(response.text)
        if response.status_code == 200:
            logger.info("Unlocking {}".format(device_id))
            return True
        else:
            logger.error("Could not unlock device")
