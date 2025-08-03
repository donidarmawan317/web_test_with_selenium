from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color
from utils import log_test_result
import time
import logging

def test_dynamic_properties(browser):
    test_name = "Dynamic Properties"
    try:
        browser.get("https://demoqa.com/dynamic-properties")
        
        # Test enabled after button
        enable_button = WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable((By.ID, "enableAfter"))
        )
        enable_button.click()
        
        # Test visible after button
        visible_button = WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located((By.ID, "visibleAfter"))
        )
        visible_button.click()
        
        # Test color change
        color_button = browser.find_element(By.ID, "colorChange")
        initial_color = color_button.value_of_css_property("color")
        
        # Wait for color to change (using explicit wait)
        WebDriverWait(browser, 15).until(
            lambda d: color_button.value_of_css_property("color") != initial_color
        )
        
        # Log success
        log_test_result(test_name, "success")
    except Exception as e:
        logging.error(f"{test_name} failed: {str(e)}")
        log_test_result(test_name, "failure")
        raise