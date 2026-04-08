import os
import pytest
from selenium import webdriver
from datetime import datetime

@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    if hasattr(request.node, "rep_call") and request.node.rep_call.outcome == "failed": 
        os.makedirs("screenshots", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join("screenshits", f"{request.node.name}_{timestamp}.png")
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":
        item.rep_call = rep