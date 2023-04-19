import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy

from pages.base_page import BasePage


class DiscoveryAndroidSearchPage(BasePage):

    SEARCH = (MobileBy.ACCESSIBILITY_ID, "Search")
    RECOMMEND = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.TextView")
    SEARCH_BAR = (MobileBy.ID, "com.discovery.discoveryplus.mobile:id/searchTextView")
    FIRST_TITLE = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.TextView")
    
    def calculate_search_click(self: "DiscoveryAndroidSearchPage") -> None:
        ts = []
        ts.append(time.time())
        self.long_wait(self.SEARCH).click()
        self.long_wait(self.RECOMMEND)
        time.sleep(2)
        ts.append(time.time())
        return ts

    def calculate_search_time(self: "DiscoveryAndroidSearchPage") -> None:
        ts = []
        ts.append(time.time())
        self.long_wait(self.SEARCH_BAR).send_keys("Shark Week")
        self.long_wait(self.FIRST_TITLE)
        time.sleep(2)
        ts.append(time.time())
        return ts
