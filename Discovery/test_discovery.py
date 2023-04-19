import os
import time
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
    api = HS_API(api_token)
    now = datetime.now()
    date_time = now.strftime("%b-%d-%Y, %H:%M:%S")

    def test_ios(self: "TestDiscovery", make_driver: MakeDriver) -> None:
        ## Driver Creation

        try:
            d: webdriver.Remote = make_driver("discovery_ios")

            splash_page = DiscoveryIOSSplashPage(d)
            splash_page.accept_pop_up()
            time.sleep(10)
            time.sleep(5)
            self.api.alert_slack_success(d.session_id, "TVOS")
        except Exception as exc:
            # failure
            try:
                self.api.alert_slack_failure(d.session_id, "TVOS", exc)
            except:
                self.api.alert_slack_failure("null", "TVOS", exc)
