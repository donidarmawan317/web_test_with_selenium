import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from utils import log_test_result

def test_button_clicks(browser):
    test_name = "Button Interactions"
    try:
        browser.get("https://demoqa.com/buttons")
        
        # Double Click
        double_click_btn = browser.find_element(By.ID, "doubleClickBtn")
        ActionChains(browser).double_click(double_click_btn).perform()
        
        # Verify with explicit wait
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "doubleClickMessage"))
        )
        
        # Right Click
        right_click_btn = browser.find_element(By.ID, "rightClickBtn")
        ActionChains(browser).context_click(right_click_btn).perform()
        
        # Verify with explicit wait
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "rightClickMessage"))
        )
        
        # Dynamic Click - use more reliable XPath
        browser.find_element(By.XPATH, "//button[text()='Click Me' and starts-with(@id, 'k')]").click()
        
        # Verify with explicit wait
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "dynamicClickMessage"))
        )
        
        log_test_result(test_name, "success")
    except Exception as e:
        logging.error(f"{test_name} failed: {str(e)}")
        log_test_result(test_name, "failure")
        raise