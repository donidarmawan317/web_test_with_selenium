import logging
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

def log_test_result(test_name, status):
    """Log test result with consistent formatting"""
    # Normalize status to lowercase
    normalized_status = status.lower()

    status_map = {
        "success": "✅ PASSED",
        "failure": "❌ FAILED",
        "error": "⚠️ ERROR"
    }
    status_text = status_map.get(normalized_status, f"UNKNOWN STATUS ({status})")
    logging.info(f"{status_text} - {test_name}")

def safe_wait(browser, condition, timeout=30, poll_frequency=0.5):
    """Robust wait function with better timeout handling"""
    try:
        return WebDriverWait(
            browser, 
            timeout,
            poll_frequency=poll_frequency
        ).until(condition)
    except TimeoutException as e:
        logging.error(f"Timeout waiting for condition: {str(e)}")
        browser.save_screenshot(f"timeout_error_{int(time.time())}.png")
        raise
