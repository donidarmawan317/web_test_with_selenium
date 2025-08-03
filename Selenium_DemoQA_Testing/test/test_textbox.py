import logging
from utils import safe_wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import log_test_result

logger = logging.getLogger(__name__)

def test_textbox_submission(browser):
    test_name = "Text Box Submission"
    try:
        browser.get("https://demoqa.com/text-box")
        
        # Fill form
        browser.find_element(By.ID, "userName").send_keys("John Doe")
        browser.find_element(By.ID, "userEmail").send_keys("john.doe@example.com")
        browser.find_element(By.ID, "currentAddress").send_keys("123 Main St")
        browser.find_element(By.ID, "permanentAddress").send_keys("456 Permanent Ave")
        
        # Submit with JavaScript to avoid interception
        submit = browser.find_element(By.ID, "submit")
        browser.execute_script("arguments[0].scrollIntoView();", submit)
        browser.execute_script("arguments[0].click();", submit)
        
        # Verify output
        output = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "output"))
        )
        output_text = output.text
        assert "John Doe" in output_text
        assert "john.doe@example.com" in output_text
        
        # Log success
        log_test_result(test_name, "success")
    except Exception as e:
        logging.error(f"{test_name} failed: {str(e)}")
        log_test_result(test_name, "failure")
        raise

def test_email_validation(browser):
    test_name = "Email Validation"
    try:
        browser.get("https://demoqa.com/text-box")
        
        # Enter invalid email
        email_field = browser.find_element(By.ID, "userEmail")
        email_field.send_keys("invalid-email")
        
        # Submit with JavaScript
        submit = browser.find_element(By.ID, "submit")
        browser.execute_script("arguments[0].scrollIntoView();", submit)
        browser.execute_script("arguments[0].click();", submit)
        
        # Verify validation error
        email_container = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#userEmail.field-error"))
        )
        
        # Log success
        log_test_result(test_name, "success")
    except Exception as e:
        logging.error(f"{test_name} failed: {str(e)}")
        log_test_result(test_name, "failure")
        raise