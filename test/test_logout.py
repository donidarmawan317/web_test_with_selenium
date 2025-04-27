from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_logout(driver):

    driver.get("https://www.saucedemo.com/")

    # Login
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    try:
        ok_button = driver.find_element("xpath", "//button[contains(text(), 'OK')]")
        ok_button.click()
    except:
        print("No password alert popup, continue...")


    # Wait until inventory page
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://www.saucedemo.com/inventory.html")
    )

    # Open side menu
    menu_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
    )
    menu_button.click()

    # Wait logout button
    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    )
    logout_button.click()
    logout_button.click()

    # Confirm back to login
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://www.saucedemo.com/")
    )
    assert driver.current_url == "https://www.saucedemo.com/", "Logout failed!"
