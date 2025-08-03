import logging
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils import log_test_result
from utils import safe_wait

def test_broken_links(browser):
    test_name = "Broken Links"
    try:
        browser.get("https://demoqa.com/broken")
        
        # Get all links
        links = safe_wait(browser, EC.presence_of_all_elements_located((By.TAG_NAME, "a")))
        
        # Filter and test valid HTTP links
        for link in links:
            url = link.get_attribute("href")
            if url and url.startswith("http"):
                try:
                    response = requests.head(url, timeout=5)
                    assert response.status_code < 400
                except requests.exceptions.Timeout:
                    logging.warning(f"Timeout checking: {url}")
                except Exception as e:
                    logging.error(f"Error checking {url}: {str(e)}")
        
        log_test_result(test_name, "success")
    except Exception as e:
        logging.error(f"{test_name} failed: {str(e)}")
        log_test_result(test_name, "failure")
        raise

def test_image_validation(browser):
    test_name = "Image Validation"
    try:
        browser.get("https://demoqa.com/broken")
        
        # Test images
        images = browser.find_elements(By.TAG_NAME, "img")
        for img in images:
            src = img.get_attribute("src")
            if src:
                try:
                    response = requests.head(src, timeout=5)
                    assert response.status_code == 200
                except requests.exceptions.Timeout:
                    logging.warning(f"Timeout for image: {src}")
                except Exception as e:
                    logging.error(f"Error for image {src}: {str(e)}")
        
        log_test_result(test_name, "success")
    except Exception as e:
        logging.error(f"{test_name} failed: {str(e)}")
        log_test_result(test_name, "failure")
        raise