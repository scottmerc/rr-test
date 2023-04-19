import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class DiscoveryAndroidTVSearchPage(BasePage):

    SEARCH = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup[4]")
    RECOMMEND = (AppiumBy.ID, "com.discovery.discoveryplus.androidtv:id/focusableViewForSearchBar")
    SEARCH_BAR = (AppiumBy.ID, "com.discovery.discoveryplus.androidtv:id/editTextAtom")
    FIRST_TITLE = (AppiumBy.ID, "com.discovery.discoveryplus.androidtv:id/textTitle")
    #FIRST_TITLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='Shark Week Classics']")
    
    def calculate_search_click(self: "DiscoveryAndroidTVSearchPage") -> None:
        ts = []
        ts.append(time.time())
        self.long_wait(self.SEARCH).click()
        self.long_wait(self.RECOMMEND)
        time.sleep(2)
        ts.append(time.time())
        return ts

    def calculate_search_time(self: "DiscoveryAndroidTVSearchPage") -> None:
        ts = []
        ts.append(time.time())
        self.long_wait(self.SEARCH_BAR).send_keys("Shark Week")
        self.long_wait(self.FIRST_TITLE)
        time.sleep(2)
        ts.append(time.time())
        return ts
