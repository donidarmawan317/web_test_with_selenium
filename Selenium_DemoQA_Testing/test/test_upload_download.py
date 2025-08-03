import logging
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import log_test_result

def test_file_download(browser):
    test_name = "File Download"
    try:
        browser.get("https://demoqa.com/upload-download")
        
        # Set download directory
        download_dir = os.path.join(os.getcwd(), "downloads")
        os.makedirs(download_dir, exist_ok=True)
        
        # Get download link source
        download_button = browser.find_element(By.ID, "downloadButton")
        file_url = download_button.get_attribute("href")
        file_name = os.path.basename(file_url)
        file_path = os.path.join(download_dir, file_name)
        
        # Delete existing file if present
        if os.path.exists(file_path):
            os.remove(file_path)
        
        # Trigger download via JavaScript
        browser.execute_script("arguments[0].click();", download_button)
        
        # Wait for download with timeout
        max_wait = 30  # seconds
        start_time = time.time()
        
        while not os.path.exists(file_path):
            if time.time() - start_time > max_wait:
                raise TimeoutError(f"File not downloaded after {max_wait} seconds")
            time.sleep(1)
        
        # Verify file size
        assert os.path.getsize(file_path) > 0, "Downloaded file is empty"
        
        log_test_result(test_name, "success")
    except Exception as e:
        logging.error(f"{test_name} failed: {str(e)}")
        log_test_result(test_name, "failure")
        raise

def test_file_upload(browser):
    test_name = "File Upload"
    try:
        browser.get("https://demoqa.com/upload-download")
        
        # Create test file
        upload_dir = os.path.join(os.getcwd(), "uploads")
        os.makedirs(upload_dir, exist_ok=True)
        upload_file = os.path.join(os.getcwd(), "test_upload.txt")
        with open(upload_file, "w") as f:
            f.write("Test file content")
        
        # Upload file
        upload_input = browser.find_element(By.ID, "uploadFile")
        upload_input.send_keys(upload_file)
        
        # Verify upload
        uploaded_path = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "uploadedFilePath"))
        ).text
        assert "test_upload.txt" in uploaded_path
        
        log_test_result(test_name, "success")
    except Exception as e:
        logging.error(f"{test_name} failed: {str(e)}")
        log_test_result(test_name, "failure")
        raise