import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    """
    This fixture is responsible for:
    - Starting the browser before each test
    - Closing the browser after each test

    Pytest automatically injects this 'driver' into any test
    that has 'driver' as a parameter.
    """

    # Create a new Chrome browser instance
    driver = webdriver.Chrome()

    # Maximize the browser window for better visibility
    driver.maximize_window()

    # Yield pauses the function here and gives control to the test
    yield driver

    # This runs AFTER the test finishes
    # It ensures the browser is always closed
    driver.quit()
