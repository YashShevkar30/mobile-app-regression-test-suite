from appium.webdriver.common.appiumby import AppiumBy


class LoginPage:
    USERNAME = (AppiumBy.ACCESSIBILITY_ID, "login_username")
    PASSWORD = (AppiumBy.ACCESSIBILITY_ID, "login_password")
    SUBMIT = (AppiumBy.ACCESSIBILITY_ID, "login_submit")
    SUCCESS_BANNER = (AppiumBy.ACCESSIBILITY_ID, "home_welcome")

    def __init__(self, driver):
        self.driver = driver

    def login(self, username: str, password: str) -> None:
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.SUBMIT).click()
