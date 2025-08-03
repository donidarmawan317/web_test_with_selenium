import logging
from common_helpers import login, handle_password_alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)

def test_cart_item_removal(driver):
    """Test item removal from cart."""
    logger.info("Starting cart removal test")
    
    # Login and add item
    driver.get("https://www.saucedemo.com/")
    login(driver)
    handle_password_alert(driver)
    
    # Add item
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@data-test,'add-to-cart')]"))
    ).click()
    
    # Go to cart
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
    ).click()
    
    # Remove item
    logger.info("Removing item from cart")
    remove_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@data-test,'remove')]"))
    )
    remove_button.click()
    
    # Verify removal
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "cart_item"))
    )
    logger.info("✅ Cart removal test passed")

def test_continue_shopping(driver):
    """Test 'Continue Shopping' functionality from cart."""
    logger.info("Starting continue shopping test")
    
    # Login and add item
    driver.get("https://www.saucedemo.com/")
    login(driver)
    handle_password_alert(driver)
    
    # Go to cart directly
    driver.get("https://www.saucedemo.com/cart.html")
    
    # Continue shopping
    logger.info("Clicking Continue Shopping")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "continue-shopping"))
    ).click()
    
    # Verify redirection
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://www.saucedemo.com/inventory.html")
    )
    assert "inventory" in driver.current_url, "Redirection failed"
    logger.info("✅ Continue shopping test passed")