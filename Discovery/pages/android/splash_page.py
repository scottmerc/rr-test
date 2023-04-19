import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy

from pages.base_page import BasePage


class DiscoveryAndroidSplashPage(BasePage):

    # SIGN_IN = (By.ID, "com.discovery.discoveryplus.androidtv:id/welcomeSignIn")
    SIGN_IN = (MobileBy.ID, "com.discovery.discoveryplus.mobile:id/welcomeSignIn")
    EMAIL = (MobileBy.ID, "com.discovery.discoveryplus.mobile:id/signInEmail")
    PASS = (MobileBy.ID, "com.discovery.discoveryplus.mobile:id/signInPassword")
    CONTINUE = (MobileBy.ID, "com.discovery.discoveryplus.mobile:id/signInContinue")
    TITLE = (MobileBy.ID, "com.discovery.discoveryplus.mobile:id/homeHeroTitleImage")

    def validate_homepage(self: "DiscoveryAndroidSplashPage") -> None:
        ts = []
        ts.append(time.time())
        # self.driver.start_activity(
        #     "com.discovery.discoveryplus.mobile",
        #     "com.discovery.plus.presentation.activities.LaunchActivity"
        #     #"com.discovery.discoveryplus.androidtv",
        #     #"com.discovery.plus.presentation.activities.TVSplashActivity",
        # )
        self.driver.activate_app("com.discovery.discoveryplus.mobile")
        sign_in = self.long_wait(self.SIGN_IN)
        time.sleep(2)
        ts.append(time.time())
        # sign_in.click()
        # time.sleep(3)
        return ts

    def calculate_sign_in_click(self: "DiscoveryAndroidSplashPage") -> None:
        ts = []
        ts.append(time.time())
        time.sleep(1)
        self.long_wait(self.SIGN_IN).click()
        self.long_wait(self.EMAIL)
        time.sleep(1)
        ts.append(time.time())
        return ts

    def calculate_sign_in_time(self: "DiscoveryAndroidSplashPage") -> None:
        ts = []
        self.long_wait(self.EMAIL).send_keys("adfree_uat_android@test.com")
        self.long_wait(self.PASS).send_keys("Adfree_uat_android123")
        time.sleep(2)
        ts.append(time.time())
        self.long_wait(self.CONTINUE).click()
        self.long_wait(self.TITLE).click()
        time.sleep(2)
        ts.append(time.time())
        return ts
