import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy

from pages.base_page import BasePage


class DiscoveryIOSLogout(BasePage):

    CLOSE = (MobileBy.ACCESSIBILITY_ID, "Close")
    BACK = (MobileBy.ACCESSIBILITY_ID, "Back")
    ACCOUNT = (MobileBy.ACCESSIBILITY_ID, "ACCOUNT")
    SIGN_OUT = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Sign Out"]')
    CONFIRM_SIGN_OUT = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Sign Out"]')

    def logout_exit(self: "DiscoveryIOSLogout") -> None:
        self.long_wait(self.CLOSE).click()
        self.long_wait(self.BACK).click()
        self.long_wait(self.BACK).click()
        self.long_wait(self.ACCOUNT).click()
        self.long_wait(self.SIGN_OUT).click()
        self.long_wait(self.CONFIRM_SIGN_OUT).click()
        # self.driver.terminate_app(
        #     "com.discovery.mobile.discoveryplus"
        # )
