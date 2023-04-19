import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy

from pages.base_page import BasePage
from random import randrange
import random


class DiscoveryIOSSplashPage(BasePage):

    Accept = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Allow"]')
    Later = (MobileBy.ACCESSIBILITY_ID, "networkLogo")
    Region = (
        MobileBy.ACCESSIBILITY_ID,
        "This app is only supported in the U S and certain U S territories.",
    )

    def accept_pop_up(self: "DiscoveryIOSSplashPage") -> None:
        try:
            self.wait(self.Accept).click()
        except:
            pass
        finally:
            self.long_wait(self.Later)

    def verify_region(self: "DiscoveryIOSSplashPage") -> None:
        try:
            self.wait(self.Accept).click()
        except:
            pass
        self.wait(self.Region)
