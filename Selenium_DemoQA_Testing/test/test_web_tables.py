import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import log_test_result
import random

def test_add_new_record(browser):
    test_name = "Add New Record"
    try:
        browser.get("https://demoqa.com/webtables")
        
        # Click Add button
        browser.find_element(By.ID, "addNewRecordButton").click()
        
        # Fill form with waits
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "firstName"))
        ).send_keys("Test")
        
        browser.find_element(By.ID, "lastName").send_keys("User")
        browser.find_element(By.ID, "userEmail").send_keys("test@example.com")
        browser.find_element(By.ID, "age").send_keys("30")
        browser.find_element(By.ID, "salary").send_keys("50000")
        browser.find_element(By.ID, "department").send_keys("QA")
        
        # Submit
        browser.find_element(By.ID, "submit").click()
        
        # Verify in table
        WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, "//div[@class='rt-tbody']"), 
                "Test"
            )
        )
        
        # Log success
        log_test_result(test_name, "success")
    except Exception as e:
        logging.error(f"{test_name} failed: {str(e)}")
        log_test_result(test_name, "failure")
        raise

def test_table_sorting(browser):
    test_name = "Table Sorting"
    try:
        browser.get("https://demoqa.com/webtables")
        
        # Click age header to sort
        browser.find_element(By.XPATH, "//div[text()='Age']").click()
        
        # Get all age values
        ages = browser.find_elements(By.XPATH, "//div[@class='rt-td'][3]")
        age_values = [int(age.text) for age in ages if age.text.strip()]
        
        # Verify sorted
        assert age_values == sorted(age_values), "Ages not sorted ascending"
        
        log_test_result(test_name, "success")
    except Exception as e:
        logging.error(f"{test_name} failed: {str(e)}")
        log_test_result(test_name, "failure")
        raise