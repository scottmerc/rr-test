import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy

from pages.base_page import BasePage


class DiscoveryIOSSearchPage(BasePage):

    SEARCH = (MobileBy.ACCESSIBILITY_ID, "SEARCH")
    RECOMMEND = (MobileBy.XPATH, "(//XCUIElementTypeStaticText[@name=\"sectionTitleLabel\"])[1]")
    SEARCH_BAR = (MobileBy.ACCESSIBILITY_ID, "searchField")
    FIRST_TITLE = (MobileBy.XPATH, "(//XCUIElementTypeStaticText[@name=\"titleLabel\"])[1]")
    
    def calculate_search_click(self: "DiscoveryIOSSearchPage") -> None:
        ts = []
        ts.append(time.time())
        self.long_wait(self.SEARCH).click()
        self.long_wait(self.RECOMMEND)
        time.sleep(2)
        ts.append(time.time())
        return ts

    def calculate_search_time(self: "DiscoveryIOSSearchPage") -> None:
        ts = []
        ts.append(time.time())
        self.long_wait(self.SEARCH_BAR).send_keys("Shark Week")
        self.long_wait(self.FIRST_TITLE)
        time.sleep(2)
        ts.append(time.time())
        return ts

    







