import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def browser():
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    # driver.set_window_size(1920, 1080)
    driver.maximize_window()
    driver.get('http://localhost:5000/')
    yield driver
    driver.quit()