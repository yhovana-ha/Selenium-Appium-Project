from selenium import webdriver
from selenium.webdriver.common.by import By

class NikeStorePage:
    def __init__(self, driver: webdriver.edge):
        """Initialize the NikeStorePage with a WebDriver instance."""
        self.driver = driver

    def store(self):
        store_container = self.driver.find_element(By.CSS_SELECTOR, "section.ncss-col-sm-12.ncss-col-md-8.ta-sm-l.pt8-sm")
        return store_container
    def store_status(self):
        store_container = self.store()
        try:
            status_element = store_container.find_element(By.CLASS_NAME, "text-color-success")
            return "Open"
        except:
            try:
                status_element = store_container.find_element(By.CLASS_NAME, "text-color-error")
                return "Closed"
            except:
                return "Status not found"

    def store_phone_number(self):
        # Locate the phone number element within the store container
        phone_element = self.store().find_element(By.CSS_SELECTOR, "div.headline-5 + p")
        phone_number = phone_element.text
        # Remove hyphens from the phone number
        phone_number = phone_number.replace("-", "")
        return phone_number
    def store_address(self):
        # Locate the address
        address_container = self.store().find_element(By.CSS_SELECTOR, "div.headline-5.pr6-sm")
        address_lines = address_container.find_elements(By.TAG_NAME, "p")
        address = "\n".join([line.text for line in address_lines])
        return address
