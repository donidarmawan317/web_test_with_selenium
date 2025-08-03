import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("demoqa_tests.log"),
        logging.StreamHandler()
    ]
)

@pytest.fixture(scope="function")
def browser():
    chrome_options = Options()
    
    # Headless configuration
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1920,1080")
    
    # Performance optimizations
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--disable-setuid-sandbox")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-logging")
    chrome_options.add_argument("--log-level=3")
    
    # Network optimizations
    chrome_options.add_argument("--disable-background-networking")
    chrome_options.add_argument("--disable-default-apps")
    chrome_options.add_argument("--disable-sync")
    chrome_options.add_argument("--metrics-recording-only")
    chrome_options.add_argument("--safebrowsing-disable-auto-update")
    chrome_options.add_argument("--disable-client-side-phishing-detection")
    
    # Timeout settings
    chrome_options.add_argument("--connection-timeout=60")
    chrome_options.add_argument("--max-time=120")
    chrome_options.page_load_strategy = 'eager'
    
    # Use WebDriver Manager for automatic driver management
    service = Service(
        ChromeDriverManager().install(),
        service_args=['--verbose'], 
        log_path='chromedriver.log'
    )
    
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Configure timeouts
    driver.set_page_load_timeout(30)
    driver.set_script_timeout(20)
    driver.implicitly_wait(5)
    
    yield driver
    
    # Clean up
    driver.quit()