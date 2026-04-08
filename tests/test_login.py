from pages.login_page import LoginPage

def test_login_success(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.enter_username("tomsmith")
    login_page.enter_password("SuperSecretPassword!")
    login_page.click_login()

    assert "Secure Area" in driver.page_source

def test_login_invalid(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.enter_username("wronguser")
    login_page.enter_password("wrongpass")
    login_page.click_login()

    assert "Your username is invalid" in driver.page_source