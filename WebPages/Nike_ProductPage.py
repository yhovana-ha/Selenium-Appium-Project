from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NikeProductPage:
    def __init__(self, driver: webdriver.Edge):
        """Initialize the NikeProductPage with a WebDriver instance."""
        self.driver = driver

    def choose_first_product(self):
        first_product = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "a.product-card__link-overlay[data-testid='product-card__link-overlay'][href='https://www.nike.com/il/t/jordan-spizike-low-shoes-lGNCtG/FQ1759-001']"))
        )
        # Scroll the element into view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", first_product)
        return first_product

    def first_product_click(self):
        # Scroll the element into view and wait for it to be clickable
        first_product = self.choose_first_product()
        # Click the first product link using JavaScript execution
        self.driver.execute_script("arguments[0].click();", first_product)

    def choose_second_product(self):
        second_product = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "a.product-card__link-overlay[data-testid='product-card__link-overlay'][href='https://www.nike.com/il/t/air-jordan-1-low-shoes-v2kdOZ/553558-092']"))
        )
        # Scroll the element into view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", second_product)
        return second_product

    def second_product_click(self):
        # Scroll the element into view and wait for it to be clickable
        second_product = self.choose_second_product()
        # Click the second product link using JavaScript execution
        self.driver.execute_script("arguments[0].click();", second_product)

    def get_product_name(self):
        product_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h1#pdp_product_title[data-testid='product_title']"))
        )
        return product_name.text

    def get_product_price(self):
        product_price = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='currentPrice-container']"))
        )
        price_text = product_price.text
        # Remove the shekel sign and convert to float
        numeric_price = float(price_text.replace('₪', '').replace(',', '').strip())
        return numeric_price
