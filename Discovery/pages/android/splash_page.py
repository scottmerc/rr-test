import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy

from pages.base_page import BasePage


class DiscoveryAndroidSplashPage(BasePage):

    TEXT = (
        MobileBy.XPATH,
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View[3]/android.view.View/android.view.View[3]/android.view.View[2]/android.view.View/android.widget.ListView/android.view.View[3]/android.view.View/android.widget.TextView[4]",
    )
    Address = (MobileBy.ACCESSIBILITY_ID, "Address Bar")

    OK = (MobileBy.ID, "com.discovery.discoplus:id/okbutton")
    LOGO = (MobileBy.ID, "com.discovery.discoplus:id/toolbarLogo")

    def navigate_to_ip(self: "DiscoveryAndroidSplashPage") -> None:
        ADDRESS = self.long_wait(self.Address)
        ADDRESS.click()
        ADDRESS.send_keys("ipinfo.io")
        self.driver.press_keycode(66)
        LOCATION = self.long_wait(self.TEXT)
        print(LOCATION.text)
        return LOCATION.text

    def validate_tv(self: "DiscoveryAndroidSplashPage") -> None:
        try:
            self.long_wait(self.OK).click()
        except:
            pass
        self.long_wait(self.LOGO)
