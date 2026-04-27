from appium import webdriver


def create_driver(platform_name: str, appium_server: str = "http://localhost:4723") -> webdriver.Remote:
    capabilities = {
        "platformName": platform_name,
        "automationName": "UiAutomator2" if platform_name.lower() == "android" else "XCUITest",
        "deviceName": "emulator",
        "app": "/path/to/app-under-test.apk",
    }
    return webdriver.Remote(appium_server, capabilities)
