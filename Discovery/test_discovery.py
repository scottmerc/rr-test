import os
import time
import json
from datetime import datetime
from appium import webdriver
from conftest import MakeDriver
from pages.android.logout import DiscoveryAndroidLogout
from pages.android.search_page import DiscoveryAndroidSearchPage
from pages.android.show_page import DiscoveryAndroidShowPage
from pages.android.speedtest_page import SpeedtestAndroidSplashPage
from pages.android.splash_page import DiscoveryAndroidSplashPage
from pages.android_tv.logout import DiscoveryAndroidTVLogout
from pages.android_tv.search_page import DiscoveryAndroidTVSearchPage
from pages.android_tv.show_page import DiscoveryAndroidTVShowPage
from pages.ios.logout import DiscoveryIOSLogout
from pages.ios.search_page import DiscoveryIOSSearchPage
from pages.ios.show_page import DiscoveryIOSShowPage
from pages.ios.splash_page import DiscoveryIOSSplashPage
from pages.ios.speedtest_page import SpeedtestIOSSplashPage
from pages.android_tv.splash_page import DiscoveryAndroidTVSplashPage


from apis.hs_apis import HS_API

from apis.hs_logger import logger, setup_logger


class TestDiscovery(object):

    api_token = os.getenv("HS_API_TOKEN")
    hostname = os.getenv("HOSTNAME")
    udid = os.getenv("UDID")
    api = HS_API(api_token)
    now = datetime.now()
    date_time = now.strftime("%b-%d-%Y, %H:%M:%S")

    def test_ios(self: "TestDiscovery", make_driver: MakeDriver) -> None:
        ## Driver Creation

        try:
            d: webdriver.Remote = make_driver("discovery_ios")

            splash_page = DiscoveryIOSSplashPage(d)
            splash_page.accept_pop_up()
            self.api.alert_slack_success(d.session_id, "TV OS")
            self.api.reliability(
                self.hostname, "passed", "Test Case Passed", self.udid, d.session_id
            )
        except Exception as exc:
            # failure
            try:
                self.api.alert_slack_failure(d.session_id, "TV OS", exc)
                self.api.reliability(
                    self.hostname, "failed", str(exc), self.udid, d.session_id
                )
            except:
                self.api.alert_slack_failure("null", "TV OS", exc)
                self.api.reliability(self.hostname, "failed", str(exc), self.udid)

    def test_firetab(self: "TestDiscovery", make_driver: MakeDriver) -> None:
        ## Driver Creation
        try:
            d: webdriver.Remote = make_driver("discovery_firetab_tv")

            splash_page = DiscoveryAndroidSplashPage(d)
            location = splash_page.navigate_to_ip()
            assert location == "London"
            caps = d.capabilities
            udid = caps["deviceUDID"]
            self.api.alert_slack_success(d.session_id, "Fire Tab")
            self.api.reliability(
                self.hostname, "passed", "Test Case Passed", udid, d.session_id
            )

        except Exception as exc:
            # failure
            try:
                self.api.alert_slack_failure(d.session_id, "Fire Tab", exc)
                self.api.reliability(
                    self.hostname, "failed", str(exc), udid, d.session_id
                )
            except:
                self.api.alert_slack_failure("null", "Fire Tab", exc)
                self.api.reliability(self.hostname, "failed", str(exc))

    def test_firetv(self: "TestDiscovery", make_driver: MakeDriver) -> None:
        ## Driver Creation
        try:
            d: webdriver.Remote = make_driver("discovery_fire_tv")

            splash_page = DiscoveryAndroidSplashPage(d)
            splash_page.validate_tv()
            caps = d.capabilities
            udid = caps["deviceUDID"]
            self.api.alert_slack_success(d.session_id, "Fire TV")
            self.api.reliability(
                self.hostname, "passed", "Test Case Passed", udid, d.session_id
            )

        except Exception as exc:
            # failure
            try:
                self.api.alert_slack_failure(d.session_id, "Fire TV", exc)
                self.api.reliability(
                    self.hostname, "failed", str(exc), udid, d.session_id
                )
            except:
                self.api.alert_slack_failure("null", "Fire TV", exc)
                self.api.reliability(self.hostname, "failed", str(exc))

    def test_ios_us(self: "TestDiscovery", make_driver: MakeDriver) -> None:
        try:
            d: webdriver.Remote = make_driver("discovery_ios_2")

            splash_page = DiscoveryIOSSplashPage(d)
            splash_page.verify_region()
            self.api.alert_slack_success(d.session_id, "TV OS")
            self.api.reliability(
                self.hostname, "passed", "Test Case Passed", self.udid, d.session_id
            )
        except Exception as exc:
            # failure
            try:
                self.api.alert_slack_failure(d.session_id, "TV OS", exc)
                self.api.reliability(
                    self.hostname, "failed", str(exc), self.udid, d.session_id
                )
            except:
                self.api.alert_slack_failure("null", "TV OS", exc)
                self.api.reliability(self.hostname, "failed", str(exc), self.udid)
