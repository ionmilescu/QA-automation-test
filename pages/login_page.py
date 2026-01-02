from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Page Object for the Login Page.

    This class contains:
    - Page URL
    - Locators
    - Actions that can be performed on the login page

    Test logic should NEVER be written here.
    """

    # URL of the login page
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, driver):
        """
        Constructor:
        - Receives the WebDriver instance
        - Initializes explicit wait
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """
        Opens the login page in the browser
        """
        self.driver.get(self.URL)

    def login(self, username, password):
        """
        Performs login action using provided credentials
        """

        # Wait until the username input is visible and type the username
        username_input = self.wait.until(
            EC.visibility_of_element_located((By.ID, "username"))
        )
        username_input.send_keys(username)

        # Find password input and type the password
        self.driver.find_element(By.ID, "password").send_keys(password)

        # Click the login button
        self.driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        ).click()
