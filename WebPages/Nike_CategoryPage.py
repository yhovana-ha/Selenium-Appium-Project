from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

class NikeCategoryPage:
    def __init__(self, driver: WebDriver):
        """Initialize the NikeCategoryPage with a WebDriver instance."""
        self.driver = driver

    def jordan_category(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a.is--link.categories__item.css-g2lskw[aria-label='Category for Jordan']")

    def jordan_click(self):
        try:
            jordan_link = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.is--link.categories__item.css-g2lskw[aria-label='Category for Jordan']"))
            )
            jordan_link.click()
        except (StaleElementReferenceException, ElementClickInterceptedException):
            jordan_link = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.is--link.categories__item.css-g2lskw[aria-label='Category for Jordan']"))
            )
            self.driver.execute_script("arguments[0].click();", jordan_link)

    def shoes_category(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a.JSftBPEZ[aria-label='Shoes']")

    def shoes_page_click(self):
        try:
            shoes_category = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.JSftBPEZ[aria-label='Shoes']"))
            )
            shoes_category.click()
        except (StaleElementReferenceException, ElementClickInterceptedException):
            shoes_category = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.JSftBPEZ[aria-label='Shoes']"))
            )
            self.driver.execute_script("arguments[0].click();", shoes_category)
