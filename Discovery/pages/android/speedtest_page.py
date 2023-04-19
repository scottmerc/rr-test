from ast import Delete
import time
from h11 import DONE
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
import re

from pages.base_page import BasePage


class SpeedtestAndroidSplashPage(BasePage):

    NEXT = (MobileBy.ID, "org.zwanoo.android.speedtest:id/welcome_message_next_button")
    CONT = (MobileBy.ID, "org.zwanoo.android.speedtest:id/permissions_continue_button")
    PERM1 = (MobileBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
    PERM2 = (MobileBy.ID, "com.android.permissioncontroller:id/permission_deny_button")
    DN_ALLOW = (MobileBy.ID, "org.zwanoo.android.speedtest:id/enable_bg_sampling_do_not_allow_button")
    DONE = (MobileBy.ID, "org.zwanoo.android.speedtest:id/gdpr_privacy_next_button")
    GO = (MobileBy.ACCESSIBILITY_ID, "Start a Speedtest")
    RESULT = (MobileBy.XPATH, '//android.widget.FrameLayout[@content-desc="DOWNLOAD"]/android.view.ViewGroup/android.widget.TextView[3]')
    #DELETE = (MobileBy.ACCESSIBILITY_ID, "Delete ALL")
    #YES = (MobileBy.ACCESSIBILITY_ID, "Yes")
    #SIDE_MENU = (MobileBy.ACCESSIBILITY_ID, "SideMenu")
    #RESULT_PAGE = (MobileBy.ACCESSIBILITY_ID, "Results")

    def capture_speed(self: "SpeedtestAndroidSplashPage") -> None:

        self.long_wait(self.NEXT).click()
        self.long_wait(self.CONT).click()
        self.long_wait(self.PERM1).click()
        self.long_wait(self.PERM2).click()
        self.long_wait(self.DN_ALLOW).click()
        self.long_wait(self.DONE).click()
        self.long_wait(self.GO).click()

        time.sleep(60)

        RESULT = self.long_wait(self.RESULT)
        speed_test_result = RESULT.text
        return speed_test_result

        # SIDE_MENU = self.long_wait(self.SIDE_MENU)
        # SIDE_MENU.click()

        # RESULT_PAGE = self.long_wait(self.RESULT_PAGE)
        # RESULT_PAGE.click()

        # RESULT = self.long_wait(self.RESULT)
        # speed_test_result = RESULT.text

        # #speed_test_result = speed_test_result.split(", ")
        # speed_test_result = speed_test_result.split("DOWNLOAD ")
        # res = re.findall(r"\d+", speed_test_result[1])

        # if len(res) > 0:
        #     return res[0]
        # else:
        #     return 0
