from selenium import webdriver
from selenium.webdriver.common.by import By
class WiseExchangeRate:
    def __init__(self, driver: webdriver.edge):
        """Initialize the NikeStorePage with a WebDriver instance."""
        self.driver = driver

    def open_wise(self):
        self.driver.get("https://wise.com/gb/currency-converter/usd-to-ils-rate")

    def get_exchange_rate(self):
        # Locate the exchange rate element on the page
        exchange_rate_element = self.driver.find_element(By.CSS_SELECTOR,"span.d-inline-block > span.text-success")
        exchange_rate = exchange_rate_element.text
        return float(exchange_rate)