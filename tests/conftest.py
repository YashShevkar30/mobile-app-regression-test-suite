import os
import pytest
from framework.driver_factory import create_driver


@pytest.fixture
def driver():
    platform = os.getenv("MOBILE_PLATFORM", "android")
    driver_instance = create_driver(platform_name=platform)
    yield driver_instance
    driver_instance.quit()
