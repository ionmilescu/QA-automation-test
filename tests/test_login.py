from pages.login_page import LoginPage


def test_valid_login(driver):
    """
    Test Case:
    Verify that a user can log in with valid credentials.

    Steps:
    1. Open login page
    2. Enter valid username and password
    3. Submit login form
    4. Verify successful login by checking URL
    """

    # Create an instance of LoginPage and pass the driver
    login_page = LoginPage(driver)

    # Open the login page
    login_page.open()

    # Perform login with valid credentials
    login_page.login("tomsmith", "SuperSecretPassword!")

    # Assert that user is redirected to secure area
    assert "secure" in driver.current_url


def test_invalid_login(driver):
    """
    Test Case:
    Verify that a user cannot log in with invalid credentials.

    Steps:
    1. Open login page
    2. Enter invalid username and password
    3. Submit login form
    4. Verify error message is displayed
    """

    # Create an instance of LoginPage and pass the driver
    login_page = LoginPage(driver)

    # Open the login page
    login_page.open()

    # Perform login with invalid credentials
    login_page.login("wrong_user", "wrong_password")

    # verify that error message is displayed
    error_message = login_page.get_error_message()
    assert "Your username is invalid!" in error_message