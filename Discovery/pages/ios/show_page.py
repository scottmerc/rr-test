import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy

from pages.base_page import BasePage


class DiscoveryIOSShowPage(BasePage):

    FIRST_TITLE = (MobileBy.XPATH, "(//XCUIElementTypeStaticText[@name=\"titleLabel\"])[1]")
    START_WATCHING = (MobileBy.ACCESSIBILITY_ID, "actionButton")
    SHOW = (MobileBy.XPATH, "(//XCUIElementTypeStaticText[@name=\"titleLabel\"])[2]")
    #SUBTITLE = (MobileBy.ACCESSIBILITY_ID, "subtitleLabel")
    PAUSE = (MobileBy.ACCESSIBILITY_ID, "pauseButton")
    
    def calculate_show_click(self: "DiscoveryIOSShowPage") -> None:
        ts = []
        ts.append(time.time())
        self.long_wait(self.FIRST_TITLE).click()
        self.long_wait(self.START_WATCHING)
        time.sleep(2)
        ts.append(time.time())
        return ts

    def calculate_show_start_time(self: "DiscoveryIOSShowPage") -> None:
        ts = []
        self.long_wait(self.START_WATCHING).click()
        time.sleep(2)
        ts.append(time.time())
        self.long_wait(self.SHOW).click()
        self.long_wait(self.PAUSE)
        time.sleep(2)
        ts.append(time.time())
        return ts






