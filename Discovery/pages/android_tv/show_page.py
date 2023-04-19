import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class DiscoveryAndroidTVShowPage(BasePage):

    FIRST_TITLE = (AppiumBy.ID, "com.discovery.discoveryplus.androidtv:id/textTitle")
    EP_INFO = (AppiumBy.ID, "com.discovery.discoveryplus.androidtv:id/tv_episode_info")
    WATCH_NOW = (AppiumBy.ID, "com.discovery.discoveryplus.androidtv:id/btnAction")
    PAUSE = (AppiumBy.ID, "com.discovery.discoveryplus.androidtv:id/player_pause")
    
    def calculate_show_click(self: "DiscoveryAndroidTVShowPage") -> None:
        ts = []
        ts.append(time.time())
        self.long_wait(self.FIRST_TITLE).click()
        self.long_wait(self.EP_INFO)
        time.sleep(2)
        ts.append(time.time())
        return ts

    def calculate_show_start_time(self: "DiscoveryAndroidTVShowPage") -> None:
        ts = []
        time.sleep(2)
        ts.append(time.time())
        self.long_wait(self.WATCH_NOW).click()
        self.long_wait(self.PAUSE)
        time.sleep(2)
        ts.append(time.time())
        return ts
