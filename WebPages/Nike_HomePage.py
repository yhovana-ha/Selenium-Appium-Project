from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class NikeHomePage:
    def __init__(self, driver: webdriver.edge):
        """Initialize the NikeHomePage with a WebDriver instance."""
        self.driver = driver
    def find_store_location(self):
        find_a_store = (self.driver.find_element(By.CSS_SELECTOR,'p[data-testid="desktop-user-menu-item-message-0"]'))
        return find_a_store
    def find_store_click(self):
        self.find_store_location().click()

    def find_men_category(self):
        men_link = self.driver.find_element(By.CSS_SELECTOR,"a.menu-hover-trigger-link[data-testid='link'][href='https://www.nike.com/il/men']")
        return men_link
    def men_page_click(self):
        self.find_men_category().click()

