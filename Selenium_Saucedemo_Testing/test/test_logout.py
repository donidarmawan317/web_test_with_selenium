from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_logout(driver):

    driver.get("https://www.saucedemo.com/")

    # Login
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # ====== PASSWORD BREACH ALERT HANDLING ======
    try:
        # Wait for warning container (modify selector based on actual HTML)
        warning_container = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//h3[contains(text(), 'Change your password')]/.."))
        )
        
        # Click either OK button or Remove link
        ok_button = warning_container.find_element(By.XPATH, ".//button[contains(text(), 'OK')]")
        ok_button.click()
        
        # Wait for warning to disappear
        WebDriverWait(driver, 3).until(
            EC.invisibility_of_element(warning_container))
        print("Dismissed password breach warning")
    except:
        print("No password alert present, continuing...")


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

    # Confirm back to login
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://www.saucedemo.com/")
    )
    assert driver.current_url == "https://www.saucedemo.com/", "Logout failed!"
