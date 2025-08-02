from selenium import webdriver
from selenium.webdriver.common.by import By

class NikeRetailPage:
    def __init__(self, driver: webdriver.edge):
        """Initialize the NikeRetailPage with a WebDriver instance."""
        self.driver = driver

    def location(self):
        location_box = self.driver.find_element(By.ID, "ta-Location_input")
        return location_box

    def input_location(self, location):
        self.location().send_keys(location)
    def first_store(self):
        return self.driver.find_element(By.CLASS_NAME,"headline-5.flex-child.flx-gro-sm-1")
    def first_store_click(self):
        self.first_store().click()
