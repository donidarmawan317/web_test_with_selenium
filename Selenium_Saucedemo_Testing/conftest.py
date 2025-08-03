import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("test_execution.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

@pytest.fixture(scope="function")
def driver():
    """Fixture to initialize and configure Chrome WebDriver."""
    logger.info("Initializing Chrome driver")
    chrome_options = Options()
    
    # Browser preferences to disable alerts
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        "profile.password_manager_leak_detection": False,
        "password_manager.onboarding_state": 2,
        "autofill.credit_card_enabled": False,
        "autofill.profile_enabled": False,
        "safebrowsing.enabled": False,
        "safebrowsing.disable_download_protection": True,
    }
    chrome_options.add_experimental_option("prefs", prefs)
    
    # Anti-bot measures
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--start-maximized")
    
    # Disable password saving prompts
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    # Initialize driver
    try:
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
        logger.info("Chrome driver initialized successfully")
    except Exception as e:
        logger.error(f"Driver initialization failed: {str(e)}")
        raise
    
    # Set global timeouts
    driver.implicitly_wait(5)
    driver.set_page_load_timeout(20)
    
    yield driver
    
    # Teardown
    logger.info("Closing browser")
    driver.quit()