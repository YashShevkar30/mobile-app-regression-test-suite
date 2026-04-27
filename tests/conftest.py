import os
import pytest
from framework.driver_factory import create_driver


@pytest.fixture
def driver():
    if os.getenv("RUN_MOBILE_E2E", "0") != "1":
        pytest.skip("Mobile E2E tests require Appium server and emulator (set RUN_MOBILE_E2E=1).")

    platform = os.getenv("MOBILE_PLATFORM", "android")
    driver_instance = create_driver(platform_name=platform)
    yield driver_instance
    driver_instance.quit()
