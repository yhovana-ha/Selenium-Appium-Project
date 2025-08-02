from appium import webdriver as mobile
from Tests.globals import CAPABILITIES_PIXEL7, APP_CALCULATOR,APPIUM_SERVER_URL_LOCAL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcAppPage:
    """
    Class for Calculator App ,finding and clicking elements inside the app.
    """
    def __init__(self, driver):
        """Initialize the CalcAppPage on Pixel7 with a WebDriver instance."""
        # Merge APP_CALCULATOR into capabilities_Pixel7 if APP_CALCULATOR contains additional capabilities
        capabilities = {**CAPABILITIES_PIXEL7, **APP_CALCULATOR}
        self.driver = mobile.Remote(APPIUM_SERVER_URL_LOCAL, capabilities)

    def input_field(self):
        input_f = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'com.google.android.calculator:id/formula')))
        return input_f

    def input_digit(self, digit):
        if digit == '.':
            digit_element_id = 'com.google.android.calculator:id/dec_point'
        else:
            digit_element_id = f'com.google.android.calculator:id/digit_{digit}'
        digit_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, digit_element_id)))
        digit_element.click()


    def input_field_sendkeys(self, number):
        for digit in str(number):
            self.input_digit(digit)



    def click_operator_plus(self):
        plus = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'com.google.android.calculator:id/op_add')))
        plus.click()

    def click_operator_divide(self):
        divide = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'com.google.android.calculator:id/op_div')))
        divide.click()

    def click_operator_equal(self):
        equal = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'com.google.android.calculator:id/eq')))
        equal.click()

    def get_result(self):
        result = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, 'com.google.android.calculator:id/result_final')))
        return result.text

    def clear_input_indicator(self):
        # Clicking outside the input field to clear the indicator
        self.driver.find_element(By.XPATH, "//android.widget.LinearLayout").click()