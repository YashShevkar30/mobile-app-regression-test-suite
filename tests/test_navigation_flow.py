from pages.home_page import HomePage
from pages.login_page import LoginPage


def test_profile_navigation(driver):
    login = LoginPage(driver)
    login.login("qa.user@example.com", "Pass@123")
    home = HomePage(driver)
    home.open_profile()
    assert home.profile_loaded()
