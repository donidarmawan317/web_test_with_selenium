from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger(__name__)

def login(driver, username="standard_user", password="secret_sauce"):
    """Perform login with given credentials."""
    logger.info(f"Logging in as {username}")
    try:
        # Navigate to login page
        driver.get("https://www.saucedemo.com/")
        
        # Enter credentials
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys(username)
        
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()
        logger.info("Login credentials submitted")
        
        # Verify successful login
        WebDriverWait(driver, 10).until(
            EC.url_contains("inventory")
        )
        logger.info("Successfully logged in and redirected to inventory page")
        return True
    except Exception as e:
        logger.error(f"Login failed: {str(e)}")
        return False

def logout(driver):
    """Perform logout from the application."""
    logger.info("Initiating logout")
    try:
        # Open menu
        menu_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
        )
        menu_button.click()
        
        # Click logout
        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
        )
        logout_button.click()
        
        # Verify logout
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://www.saucedemo.com/")
        )
        logger.info("Logout completed successfully")
        return True
    except Exception as e:
        logger.error(f"Logout failed: {str(e)}")
        return False