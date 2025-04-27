from selenium.webdriver.common.by import By
import time

def test_successful_login(driver):
    
    # Navigate to the SauceDemo login page
    driver.get("https://www.saucedemo.com/")
    
    # Locate username, password fields, and login button, then perform login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # Wait briefly for the page transition
    time.sleep(2)
    
    # Assert that the browser has navigated to the inventory page
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Login did not redirect to inventory page"
