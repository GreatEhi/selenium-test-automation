import pytest
import json
from pages.login_page import LoginPage

def load_test_data():
    with open("data/login_data.json") as f:
        return json.load(f)

@pytest.mark.parametrize("data", load_test_data())
def test_login(driver, data):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.enter_username(data["username"])
    login_page.enter_password(data["password"])
    login_page.click_login()

    assert data["expected"] in driver.page_source