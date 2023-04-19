import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy

from pages.base_page import BasePage


class DiscoveryAndroidShowPage(BasePage):

    FIRST_TITLE = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.TextView")
    START_WATCHING = (MobileBy.ID, "com.discovery.discoveryplus.mobile:id/cta_button")
    SHOW = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.TextView")
    PAUSE = (MobileBy.ID, "com.discovery.discoveryplus.mobile:id/player_pause")
    
    def calculate_show_click(self: "DiscoveryAndroidShowPage") -> None:
        ts = []
        ts.append(time.time())
        self.long_wait(self.FIRST_TITLE).click()
        self.long_wait(self.START_WATCHING)
        time.sleep(2)
        ts.append(time.time())
        return ts

    def calculate_show_start_time(self: "DiscoveryAndroidShowPage") -> None:
        ts = []
        self.long_wait(self.START_WATCHING).click()
        time.sleep(2)
        ts.append(time.time())
        self.long_wait(self.SHOW).click()
        self.long_wait(self.PAUSE)
        time.sleep(2)
        ts.append(time.time())
        return ts
