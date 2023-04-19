import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class DiscoveryAndroidTVLogout(BasePage):

    ACCOUNT = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup[5]")
    SIGN_OUT = (AppiumBy.ID, "com.discovery.discoveryplus.androidtv:id/btnSignOut")
    CONFIRM_SIGN_OUT = (AppiumBy.ID, "com.discovery.discoveryplus.androidtv:id/buttonPositive")

    def logout_exit(self: "DiscoveryAndroidTVLogout") -> None:
        self.driver.press_keycode(4)
        self.driver.press_keycode(4)
        self.long_wait(self.ACCOUNT).click()
        time.sleep(2)
        self.driver.press_keycode(22)
        self.driver.press_keycode(22)
        self.driver.press_keycode(22)
        self.long_wait(self.SIGN_OUT).click()
        self.long_wait(self.SIGN_OUT).click()
        self.long_wait(self.CONFIRM_SIGN_OUT).click()
        self.long_wait(self.CONFIRM_SIGN_OUT).click()
        self.driver.terminate_app(
            "com.discovery.discoveryplus.androidtv"
        )







