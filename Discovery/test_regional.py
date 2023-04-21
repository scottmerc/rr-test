import os
import time
import json
from datetime import datetime
from apis.hs_apis import HS_API
import random

from apis.hs_logger import logger, setup_logger


class TestRegional(object):

    api_token = os.getenv("HS_API_TOKEN")
    hostname = os.getenv("HOSTNAME")
    udid = os.getenv("UDID")
    api = HS_API(api_token)
    geos = [
        "mx-mex",
        "nl-hag",
        "ie-dub",
        "default",
        "us-east-1",
        "br-sao",
        "us-west-1",
        "us-nje",
        "se-sto",
        "gb-lhr",
        "ph-mnl",
        "eu-west-2",
        "us-nyc",
        "fi-hel",
        "ap-south-1",
        "local",
        "de-fra",
        "ca-tor",
        "es-bio",
    ]

    def test_tizen(self: "TestRegional"):
        hosts = [
            "dev-ca-tor-2-proxy-14-lin.headspin.io",
            "dev-ca-tor-2-proxy-22-lin.headspin.io",
            "dev-us-pao-20-proxy-26-lin.headspin.io",
            "dev-us-pao-20-proxy-9-lin.headspin.io",
            "dev-us-sny-7-proxy-3-lin.headspin.io",
            "dev-us-sny-9-proxy-3-lin.headspin.io",
        ]
        models = "tizen"

        for host in hosts:
            r = self.api.lock_devices(host, models)
            time.sleep(10)
            if r != False:
                geo = random.choice(self.geos)
                device_address = r["device_id"] + "@" + r["hostname"]
                logger.info("{} Locked".format(device_address))
                success, message = self.api.regional_routing(device_address, geo)
                if success == True:
                    msg = "{} successfully set tunnel to {}".format(device_address, geo)
                    logger.info(msg)
                    self.api.reliability(host, "passed", msg, r["device_id"])
                else:
                    msg = "{} failed to set tunnel to {}: {}".format(
                        device_address, geo, message
                    )
                    logger.error(msg)
                    self.api.reliability(host, "failed", msg, r["device_id"])
                time.sleep(10)
                self.api.unlock_devices(host, models)
                logger.info("{} Unlocked".format(device_address))
                time.sleep(15)
            else:
                logger.error("No device on {} could be locked".format(host))
                pass

    def test_roku(self: "TestRegional"):
        hosts = [
            "dev-ca-tor-2-proxy-14-lin.headspin.io",
            "dev-us-pao-20-proxy-2-lin.headspin.io",
            "dev-us-pao-20-proxy-3-lin.headspin.io",
            "dev-us-sny-7-proxy-3-lin.headspin.io",
            "dev-us-sny-9-proxy-10-lin.headspin.io",
            "dev-us-sny-9-proxy-13-lin.headspin.io",
            "dev-us-sny-9-proxy-3-lin.headspin.io",
        ]
        models = "roku"

        for host in hosts:
            r = self.api.lock_devices(host, models)
            time.sleep(10)
            if r != False:
                geo = random.choice(self.geos)
                device_address = r["device_id"] + "@" + r["hostname"]
                logger.info("{} Locked".format(device_address))
                success, message = self.api.regional_routing(device_address, geo)
                if success == True:
                    msg = "{} successfully set tunnel to {}".format(device_address, geo)
                    logger.info(msg)
                    self.api.reliability(host, "passed", msg, r["device_id"])
                else:
                    msg = "{} failed to set tunnel to {}: {}".format(
                        device_address, geo, message
                    )
                    logger.error(msg)
                    self.api.reliability(host, "failed", msg, r["device_id"])
                time.sleep(10)
                self.api.unlock_devices(host, models)
                logger.info("{} Unlocked".format(device_address))
                time.sleep(15)
            else:
                logger.error("No device on {} could be locked".format(host))
                pass

    def test_lg(self: "TestRegional"):
        hosts = [
            "dev-ca-tor-2-proxy-14-lin.headspin.io",
            "dev-us-pao-20-proxy-9-lin.headspin.io",
            "dev-us-sny-9-proxy-2-lin.headspin.io",
            "dev-us-sny-9-proxy-5-lin.headspin.io",
        ]
        models = "lgtv"

        for host in hosts:
            r = self.api.lock_devices(host, models)
            time.sleep(10)
            if r != False:
                geo = random.choice(self.geos)
                device_address = r["device_id"] + "@" + r["hostname"]
                logger.info("{} Locked".format(device_address))
                success, message = self.api.regional_routing(device_address, geo)
                if success == True:
                    msg = "{} successfully set tunnel to {}".format(device_address, geo)
                    logger.info(msg)
                    self.api.reliability(host, "passed", msg, r["device_id"])
                else:
                    msg = "{} failed to set tunnel to {}: {}".format(
                        device_address, geo, message
                    )
                    logger.error(msg)
                    self.api.reliability(host, "failed", msg, r["device_id"])
                time.sleep(10)
                self.api.unlock_devices(host, models)
                logger.info("{} Unlocked".format(device_address))
                time.sleep(15)
            else:
                logger.error("No device on {} could be locked".format(host))
                pass

    def test_vizio(self: "TestRegional"):
        hosts = [
            "dev-ca-tor-2-proxy-14-lin.headspin.io",
            "dev-ca-tor-2-proxy-17-lin.headspin.io",
            "dev-us-pao-20-proxy-26-lin.headspin.io",
            "dev-us-pao-20-proxy-28-lin.headspin.io",
            "dev-us-pao-20-proxy-9-lin.headspin.io",
        ]
        models = "vizio"

        for host in hosts:
            r = self.api.lock_devices(host, models)
            time.sleep(10)
            if r != False:
                geo = random.choice(self.geos)
                device_address = r["device_id"] + "@" + r["hostname"]
                logger.info("{} Locked".format(device_address))
                success, message = self.api.regional_routing(device_address, geo)
                if success == True:
                    msg = "{} successfully set tunnel to {}".format(device_address, geo)
                    logger.info(msg)
                    self.api.reliability(host, "passed", msg, r["device_id"])
                else:
                    msg = "{} failed to set tunnel to {}: {}".format(
                        device_address, geo, message
                    )
                    logger.error(msg)
                    self.api.reliability(host, "failed", msg, r["device_id"])
                time.sleep(10)
                self.api.unlock_devices(host, models)
                logger.info("{} Unlocked".format(device_address))
                time.sleep(15)
            else:
                logger.error("No device on {} could be locked".format(host))
                pass

    def test_xbox(self: "TestRegional"):
        hosts = [
            "dev-ca-tor-2-proxy-15-lin.headspin.io",
            "dev-us-pao-20-proxy-9-lin.headspin.io",
        ]
        models = "xbox_series_s"

        for host in hosts:
            r = self.api.lock_devices(host, models)
            time.sleep(10)
            if r != False:
                geo = random.choice(self.geos)
                device_address = r["device_id"] + "@" + r["hostname"]
                logger.info("{} Locked".format(device_address))
                success, message = self.api.regional_routing(device_address, geo)
                if success == True:
                    msg = "{} successfully set tunnel to {}".format(device_address, geo)
                    logger.info(msg)
                    self.api.reliability(host, "passed", msg, r["device_id"])
                else:
                    msg = "{} failed to set tunnel to {}: {}".format(
                        device_address, geo, message
                    )
                    logger.error(msg)
                    self.api.reliability(host, "failed", msg, r["device_id"])
                time.sleep(10)
                self.api.unlock_devices(host, models)
                logger.info("{} Unlocked".format(device_address))
                time.sleep(15)
            else:
                logger.error("No device on {} could be locked".format(host))
                pass
