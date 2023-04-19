import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
#from appium.webdriver.common.AppiumBy import AppiumBy

from pages.base_page import BasePage


class DiscoveryAndroidLogout(BasePage):

    SCREEN = (AppiumBy.ID, "com.discovery.discoveryplus.mobile:id/loading_view_layout_id")
    CLOSE = (AppiumBy.ID, "com.discovery.discoveryplus.mobile:id/player_back_button")
    ACCOUNT = (AppiumBy.ACCESSIBILITY_ID, "Account")
    SIGN_OUT = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[2]/android.widget.FrameLayout[5]/android.view.ViewGroup/android.widget.TextView")
    CONFIRM_SIGN_OUT = (AppiumBy.ID, "android:id/button1")

    def logout_exit(self: "DiscoveryAndroidLogout") -> None:
        self.long_wait(self.SCREEN).click()
        self.long_wait(self.CLOSE).click()
        self.driver.back()
        self.driver.back()
        self.long_wait(self.ACCOUNT).click()
        self.long_wait(self.SIGN_OUT).click()
        self.long_wait(self.CONFIRM_SIGN_OUT).click()
        self.driver.terminate_app(
            "com.discovery.discoveryplus.mobile"
        )







