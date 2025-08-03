import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import log_test_result

def test_checkbox_selection(browser):
    test_name = "Checkbox Selection"
    try:
        browser.get("https://demoqa.com/checkbox")
        
        # Expand all checkboxes
        expand_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.rct-option-expand-all"))
        )
        expand_button.click()
        
        # Select specific checkboxes
        selections = [
            ("desktop", "Desktop"),
            ("documents", "Documents"),
            ("workspace", "Workspace"),
            ("office", "Office")
        ]
        
        # Click and verify each checkbox
        for cb_id, cb_name in selections.items():
            # Use JavaScript to ensure checkbox is clickable
            checkbox = browser.find_element(By.ID, f"tree-node-{cb_id}")
            browser.execute_script("arguments[0].scrollIntoView();", checkbox)
            browser.execute_script("arguments[0].click();", checkbox)
            
            # Verify selection immediately
            assert checkbox.is_selected(), f"Checkbox {cb_name} not selected"
        
        # Verify all in results
        result = browser.find_element(By.ID, "result")
        result_text = result.text.lower()
        
        for cb_name in selections.values():
            assert cb_name.lower() in result_text, f"{cb_name} not found in results"
        
        log_test_result(test_name, "success")
    except Exception as e:
        logging.error(f"{test_name} failed: {str(e)}")
        log_test_result(test_name, "failure")
        raise

def test_partial_selection(browser):
    """Test partial selection states in tree hierarchy"""
    test_name = "Partial Selection"
    try:
        browser.get("https://demoqa.com/checkbox")

        # Expand Documents
        documents_arrow = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Documents']/preceding-sibling::button"))
        )
        documents_arrow.click()

        # Select specific child elements
        selections = [
            ("react", "React"),
            ("angular", "Angular"),
            ("vue", "Vue"),
        ]

        for cb_id, cb_name in selections.items():
            # Use JavaScript to click
            checkbox = browser.find_element(By.ID, f"tree-node-{cb_id}")
            browser.execute_script("arguments[0].scrollIntoView();", checkbox)
            browser.execute_script("arguments[0].click();", checkbox)
            
            # Verify selection
            assert checkbox.is_selected(), f"Checkbox {cb_name} not selected"
        
        # Verify in results
        result = browser.find_element(By.ID, "result")
        result_text = result.text.lower()
        
        for cb_name in selections.values():
            assert cb_name.lower() in result_text, f"{cb_name} not found in results"
        log_test_result(test_name, "success")
    except Exception as e:
        logging.error(f"{test_name} failed: {str(e)}")
        log_test_result(test_name, "failure")
        raise