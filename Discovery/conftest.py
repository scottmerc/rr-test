import pytest
import json
import os
import logging
from appium import webdriver
from typing import Callable
from apis.hs_logger import logger, setup_logger
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

setup_logger(logger, logging.DEBUG)

api_token = os.getenv("HS_API_TOKEN")
host = os.getenv("HOSTNAME")

MakeDriver = Callable[[str], webdriver.Remote]

DISCOVERY_ANDROID_CAPS = {
    "udid": "RF8M33Y55YM",
    "autoAcceptAlerts": True,
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "headspin:capture.video": True,
    "newCommandTimeout": 300,
    "appPackage": "org.zwanoo.android.speedtest",
    "appActivity": "com.ookla.mobile4.screens.main.MainActivity",
}

# DISCOVERY_ANDROID_TV_CAPS = {
#     "appium:deviceName": "Pixel 4",
#     "appium:udid": "9B061FFAZ00236",
#     "headspin:waitForAvailableTimeout": 240,
#     "headspin:capture.video": True,
#     "appium:autoAcceptAlerts": True,
#     "appium:automationName": "UiAutomator2",
#     "appium:newCommandTimeout": 180,
#     "headspin:app.id": "9ce7b167-2e8e-42c1-8b5d-a6eca1e16151",
#     "appium:appPackage": "com.wbd.stream",
#     "appium:platformName": "android",
#     "appium:appActivity": "com.wbd.stream.MainActivity",
#     "appium:fullReset": True,
# }

DISCOVERY_IOS_CAPS = {
    "appium:deviceName": "Apple TV 4K",
    "appium:udid": "99ff9bdd142aec39d5bf86ec3c8a29d508aa9133",
    "appium:automationName": "xcuitest",
    "appium:platformVersion": "16.4",
    "platformName": "tvos",
    "appium:bundleId": "com.discovery.mobile.enterprise.tlc",
    "headspin:capture.video": True,
    "headspin:network.regionalRouting": "us-west-1",
    # "appium:noReset": True,
    # "headspin:app.id": "2e78112c3e7c4c69911d9bc1402ee9f9",
    # "headspin:controlLock": True,
    "newCommandTimeout": 300,
    "appium:autoAcceptAlerts": True,
    "headspin:selector": {"host": host}
    # "headspin:capture.ignoreHosts": [".*"],
}

DISCOVERY_FIRETAB_CAPS = {
    "appium:deviceName": "Fire Tab",
    "headspin:capture.video": True,
    "headspin:network.regionalRouting": "us-west-1",
    "appium:udid": "GCC19D06212208W0",
    "appium:autoAcceptAlerts": False,
    "appium:automationName": "Appium",
    "headspin:newCommandTimeout": 300,
    "appium:newCommandTimeout": 300,
    "appium:appPackage": "com.hbo.hbonow",
    "platformName": "Android",
    "appium:appActivity": "com.wbd.stream.MainActivity",
    # "headspin:controlLock": True,
    # "headspin:capture.ignoreHosts": [".*"],
}


@pytest.fixture
def make_driver() -> webdriver.Remote:
    driver = None

    def _make_driver(app: str) -> webdriver.Remote:
        nonlocal driver
        if app == "discovery_android":
            caps = DISCOVERY_ANDROID_CAPS
            url = "https://dev-us-pao-20.headspin.io:7012/v0/{}/wd/hub".format(
                api_token
            )
        elif app == "discovery_ios":
            caps = DISCOVERY_IOS_CAPS
            url = "https://appium-dev.headspin.io:443/v0/{}/wd/hub".format(api_token)
        # elif app == "discovery_android_tv":
        #     caps = DISCOVERY_ANDROID_TV_CAPS
        #     url = "https://appium-dev.headspin.io:443/v0/{}/wd/hub".format(api_token)
        elif app == "discovery_firetab_tv":
            caps = DISCOVERY_FIRETAB_CAPS
            url = "https://appium-dev.headspin.io:443/v0/{}/wd/hub".format(api_token)
        driver = webdriver.Remote(
            command_executor=url, desired_capabilities=caps, direct_connection=True
        )
        logger.info("\n {}".format(json.dumps(caps, indent=2)))
        return driver

    yield _make_driver
    driver.quit()
