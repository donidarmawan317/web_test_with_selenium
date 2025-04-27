from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_full_checkout(driver):
    
    driver.get("https://www.saucedemo.com/")
    
    # ====== LOGIN ======
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    try:
        ok_button = driver.find_element("xpath", "//button[contains(text(), 'OK')]")
        ok_button.click()
    except:
        print("No password alert popup, continue...")


    # ====== INVENTORY PAGE ======
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://www.saucedemo.com/inventory.html")
    )

    # Add first product to cart
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add to cart')]"))
    )
    add_to_cart_button.click()

    # Go to cart
    cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_icon.click()

    # ====== CART PAGE ======
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://www.saucedemo.com/cart.html")
    )

    # Click Checkout
    checkout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )
    checkout_button.click()

    # ====== YOUR INFORMATION PAGE ======
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://www.saucedemo.com/checkout-step-one.html")
    )

    # Fill in First Name, Last Name, Postal Code
    driver.find_element(By.ID, "first-name").send_keys("Doni")
    driver.find_element(By.ID, "last-name").send_keys("Testing")
    driver.find_element(By.ID, "postal-code").send_keys("12345")

    # Click Continue
    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    # ====== OVERVIEW PAGE ======
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://www.saucedemo.com/checkout-step-two.html")
    )

    # Click Finish
    finish_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "finish"))
    )
    finish_button.click()

    # ====== COMPLETE PAGE ======
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://www.saucedemo.com/checkout-complete.html")
    )

    # Click Back Home
    back_home_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "back-to-products"))
    )
    back_home_button.click()

    # ====== FINAL CHECK ======
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://www.saucedemo.com/inventory.html")
    )
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Did not return to inventory!"

    print("✅ Test Passed: Full checkout flow completed successfully.")
