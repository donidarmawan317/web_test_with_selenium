from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def create_chrome_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    # Add other options if you want (like headless, disable infobars, etc.)
    
    driver = webdriver.Chrome(options=chrome_options)
    return driver