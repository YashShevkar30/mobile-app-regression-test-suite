from appium.webdriver.common.appiumby import AppiumBy
from framework.waits import wait_for_visible


class LoginPage:
    USERNAME = (AppiumBy.ACCESSIBILITY_ID, "login_username")
    USERNAME_FALLBACK = (AppiumBy.ID, "com.sample.app:id/login_username")
    PASSWORD = (AppiumBy.ACCESSIBILITY_ID, "login_password")
    SUBMIT = (AppiumBy.ACCESSIBILITY_ID, "login_submit")
    SUCCESS_BANNER = (AppiumBy.ACCESSIBILITY_ID, "home_welcome")

    def __init__(self, driver):
        self.driver = driver

    def _find_username(self):
        try:
            return wait_for_visible(self.driver, self.USERNAME, timeout=8)
        except Exception:
            return wait_for_visible(self.driver, self.USERNAME_FALLBACK, timeout=8)

    def login(self, username: str, password: str) -> None:
        self._find_username().send_keys(username)
        wait_for_visible(self.driver, self.PASSWORD).send_keys(password)
        wait_for_visible(self.driver, self.SUBMIT).click()
