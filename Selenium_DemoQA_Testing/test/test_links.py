import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import log_test_result

def test_simple_links(browser):
    test_name = "Simple Links"
    try:
        browser.get("https://demoqa.com/links")
        
        for link_id in ["simpleLink", "dynamicLink"]:
            original_window = browser.current_window_handle
            browser.find_element(By.ID, link_id).click()
            
            # Switch to new tab
            WebDriverWait(browser, 5).until(lambda d: len(d.window_handles) > 1)
            browser.switch_to.window(browser.window_handles[1])
            assert "demoqa.com" in browser.current_url.lower()
            browser.close()
            browser.switch_to.window(original_window)
        
        log_test_result(test_name, "success")
    except Exception as e:
        logging.error(f"{test_name} failed: {str(e)}")
        log_test_result(test_name, "failure")
        raise

def test_api_links(browser):
    test_name = "API Links"
    try:
        browser.get("https://demoqa.com/links")
        
        api_links = {
            "created": (201, "Created"),
            "no-content": (204, "No Content"),
            "moved": (301, "Moved Permanently"),
            "bad-request": (400, "Bad Request"),
            "unauthorized": (401, "Unauthorized"),
            "forbidden": (403, "Forbidden"),
            "invalid-url": (404, "Not Found")
        }
        
        for link_id, (status_code, status_text) in api_links.items():
            # Scroll to and click the link
            link = browser.find_element(By.ID, link_id)
            browser.execute_script("arguments[0].scrollIntoView();", link)
            link.click()
            
            # Wait for and get the response element
            response_element = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.ID, "linkResponse"))
            )
            
            # Get the response text once
            response_text = response_element.text
            
            # Verify both status code and text in the response
            assert str(status_code) in response_text, (
                f"Status code {status_code} not found in response: {response_text}"
            )
            assert status_text in response_text, (
                f"Status text '{status_text}' not found in response: {response_text}"
            )
        
        log_test_result(test_name, "success")
    except Exception as e:
        logging.error(f"{test_name} failed: {str(e)}")
        log_test_result(test_name, "failure")
        raise