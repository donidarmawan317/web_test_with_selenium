import logging
from selenium.webdriver.common.by import By
from utils import log_test_result

def test_radio_button_selection(browser):
    test_name = "Radio Button Selection"
    try:
        browser.get("https://demoqa.com/radio-button")
        
        # Test Yes radio
        browser.find_element(By.CSS_SELECTOR, "label[for='yesRadio']").click()
        result = browser.find_element(By.CSS_SELECTOR, ".text-success")
        assert "Yes" in result.text
        
        # Test Impressive radio
        browser.find_element(By.CSS_SELECTOR, "label[for='impressiveRadio']").click()
        result = browser.find_element(By.CSS_SELECTOR, ".text-success")
        assert "Impressive" in result.text
        
        log_test_result(test_name, "success")
    except Exception as e:
        logging.error(f"{test_name} failed: {str(e)}")
        log_test_result(test_name, "failure")
        raise

def test_radio_button_disabled(browser):
    test_name = "Radio Button Disabled"
    try:
        browser.get("https://demoqa.com/radio-button")
        
        # Verify No radio is disabled
        no_radio = browser.find_element(By.ID, "noRadio")
        assert not no_radio.is_enabled()
        
        log_test_result(test_name, "success")
    except Exception as e:
        logging.error(f"{test_name} failed: {str(e)}")
        log_test_result(test_name, "failure")
        raise