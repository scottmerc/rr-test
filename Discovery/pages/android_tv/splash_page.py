import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class DiscoveryAndroidTVSplashPage(BasePage):

    SIGN_IN = (By.ID, "com.discovery.discoveryplus.androidtv:id/welcomeSignIn")
    EMAIL = (AppiumBy.ID, "com.discovery.discoveryplus.androidtv:id/emailField")
    PASS = (AppiumBy.ID, "com.discovery.discoveryplus.androidtv:id/passwordField")
    SHOW = (AppiumBy.ID, "com.discovery.discoveryplus.androidtv:id/showAction")
    CONTINUE = (AppiumBy.ID, "com.discovery.discoveryplus.androidtv:id/signInAction")
    TITLE = (AppiumBy.ID, "com.discovery.discoveryplus.androidtv:id/btnHeroAction")

    def calculate_sign_in_click(self: "DiscoveryAndroidTVSplashPage") -> None:
        ts = []
        self.long_wait(self.SIGN_IN).click()
        ts.append(time.time())
        time.sleep(2)
        self.long_wait(self.SIGN_IN).click()
        self.long_wait(self.EMAIL)
        time.sleep(2)
        ts.append(time.time())
        return ts

    def calculate_sign_in_time(self: "DiscoveryAndroidTVSplashPage") -> None:
        ts = []
        self.long_wait(self.EMAIL).send_keys("scott@headspin.io")
        self.long_wait(self.PASS).send_keys("SpinHead12!")
        self.long_wait(self.SHOW).click()
        time.sleep(2)
        ts.append(time.time())
        self.long_wait(self.CONTINUE).click()
        self.long_wait(self.CONTINUE).click()
        self.long_wait(self.TITLE).click()
        time.sleep(2)
        ts.append(time.time())
        return ts
