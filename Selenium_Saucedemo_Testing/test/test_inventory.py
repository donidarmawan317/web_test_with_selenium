from common_helpers import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import logging
import time

logger = logging.getLogger(__name__)

def test_product_sorting(driver):
    """Test inventory sorting functionality."""
    logger.info("Starting inventory sorting test")
    
    # Login
    login(driver)
    
    # Wait for products to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
    )
    
    # Get initial product names
    product_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    initial_names = [product.text for product in product_elements]
    
    # Sort products (Z-A)
    logger.info("Sorting products Z-A")
    sort_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    Select(sort_dropdown).select_by_value("za")
    
    # Wait for sorting to complete
    time.sleep(1)  # Allow time for UI update
    WebDriverWait(driver, 10).until(
        lambda d: d.find_element(By.CLASS_NAME, "inventory_item_name").text != initial_names[0]
    )
    
    # Get sorted product names
    product_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    sorted_names = [product.text for product in product_elements]
    
    # Verify sorted order
    expected_sorted = sorted(initial_names, reverse=True)
    assert sorted_names == expected_sorted, \
        f"Products not sorted Z-A properly.\nExpected: {expected_sorted}\nActual: {sorted_names}"
    logger.info("✅ Sorting test passed")

def test_add_multiple_items(driver):
    """Test adding multiple items to cart."""
    logger.info("Starting multiple items test")
    
    # Login
    login(driver)
    
    # Add 3 items
    logger.info("Adding items to cart")
    add_buttons = driver.find_elements(By.XPATH, "//button[contains(@data-test,'add-to-cart')]")
    for i in range(min(3, len(add_buttons))):
        add_buttons[i].click()
    
    # Verify cart count
    cart_badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert cart_badge.text == "3", "Cart count mismatch"
    logger.info("✅ Multiple items test passed")