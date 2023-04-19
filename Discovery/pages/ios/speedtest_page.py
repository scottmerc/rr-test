from ast import Delete
import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
import re

from pages.base_page import BasePage


class SpeedtestIOSSplashPage(BasePage):

    GO = (MobileBy.ACCESSIBILITY_ID, "GO")
    RESULT = (
        By.XPATH,
        '(//XCUIElementTypeCell[@name="ResultCell"])[1]',
    )
    DELETE = (MobileBy.ACCESSIBILITY_ID, "Delete ALL")
    YES = (MobileBy.ACCESSIBILITY_ID, "Yes")
    SIDE_MENU = (MobileBy.ACCESSIBILITY_ID, "SideMenu")
    RESULT_PAGE = (MobileBy.ACCESSIBILITY_ID, "Results")

    def capture_speed(self: "SpeedtestIOSSplashPage") -> None:

        GO = self.long_wait(self.GO)
        GO.click()

        time.sleep(60)

        SIDE_MENU = self.long_wait(self.SIDE_MENU)
        SIDE_MENU.click()

        RESULT_PAGE = self.long_wait(self.RESULT_PAGE)
        RESULT_PAGE.click()

        RESULT = self.long_wait(self.RESULT)
        speed_test_result = RESULT.text

        #speed_test_result = speed_test_result.split(", ")
        speed_test_result = speed_test_result.split("DOWNLOAD ")
        res = re.findall(r"\d+", speed_test_result[1])

        if len(res) > 0:
            return res[0]
        else:
            return 0
