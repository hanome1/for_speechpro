import pytest

from driver import Driver


@pytest.fixture(autouse=True, scope='session')
def browser() -> Driver:
    driver = Driver()
    # driver.set_window_size(1920, 1080)
    driver.get("http://localhost:5000/")

    yield driver

    try:
        driver.quit()
    finally:
        driver.__class__._instances = {}