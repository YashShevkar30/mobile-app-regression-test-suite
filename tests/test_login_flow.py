from pages.login_page import LoginPage


def test_login_smoke(driver):
    page = LoginPage(driver)
    page.login("qa.user@example.com", "Pass@123")
    assert driver.find_element(*LoginPage.SUCCESS_BANNER).is_displayed()
