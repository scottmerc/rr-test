import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy

from pages.base_page import BasePage
from random import randrange
import random


class DiscoveryIOSSplashPage(BasePage):

    Accept = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Allow"]')
    Later = (MobileBy.ACCESSIBILITY_ID, "networkLogo")

    def accept_pop_up(self: "DiscoveryIOSSplashPage") -> None:
        # self.long_wait(self.Accept).click()
        self.long_wait(self.Later)
