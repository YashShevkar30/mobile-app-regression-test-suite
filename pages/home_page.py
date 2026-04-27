from appium.webdriver.common.appiumby import AppiumBy
from framework.waits import wait_for_visible


class HomePage:
    PROFILE_TAB = (AppiumBy.ACCESSIBILITY_ID, "tab_profile")
    PROFILE_HEADER = (AppiumBy.ACCESSIBILITY_ID, "profile_header")

    def __init__(self, driver):
        self.driver = driver

    def open_profile(self):
        wait_for_visible(self.driver, self.PROFILE_TAB).click()

    def profile_loaded(self) -> bool:
        return wait_for_visible(self.driver, self.PROFILE_HEADER).is_displayed()
