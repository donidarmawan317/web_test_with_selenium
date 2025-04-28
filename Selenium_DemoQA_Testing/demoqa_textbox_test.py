import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestDemoQATextBox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/text-box")
        self.wait = WebDriverWait(self.driver, 10)

    def test_text_box_submission(self):
        # Test data
        test_data = {
            "full_name": "John Doe",
            "email": "john.doe@example.com",
            "current_address": "123 Main Street, Apt 4B\nNew York City",
            "permanent_address": "456 Oak Road\nSuite 22\nLos Angeles"
        }

        # Locate elements
        full_name_field = self.wait.until(EC.presence_of_element_located((By.ID, "userName")))
        email_field = self.driver.find_element(By.ID, "userEmail")
        current_address_field = self.driver.find_element(By.ID, "currentAddress")
        permanent_address_field = self.driver.find_element(By.ID, "permanentAddress")
        submit_button = self.driver.find_element(By.ID, "submit")

        # Fill out form
        full_name_field.send_keys(test_data["full_name"])
        email_field.send_keys(test_data["email"])
        current_address_field.send_keys(test_data["current_address"])
        permanent_address_field.send_keys(test_data["permanent_address"])

        # Submit form
        self.driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        submit_button.click()

        # Verify output
        output_section = self.wait.until(EC.visibility_of_element_located((By.ID, "output")))
        
        output_name = output_section.find_element(By.ID, "name").text
        output_email = output_section.find_element(By.ID, "email").text
        output_current_address = output_section.find_element(By.ID, "currentAddress").text
        output_permanent_address = output_section.find_element(By.ID, "permanentAddress").text

        # Assert results
        self.assertIn(test_data["full_name"], output_name)
        self.assertIn(test_data["email"], output_email)
        self.assertIn(test_data["current_address"].replace("\n", " "), output_current_address)
        self.assertIn(test_data["permanent_address"].replace("\n", " "), output_permanent_address)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()