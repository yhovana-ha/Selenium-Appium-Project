from appium import webdriver as mobile
from Tests.globals import CAPABILITIES_PIXEL7, APP_CALLER,APPIUM_SERVER_URL_LOCAL
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CallerAppPage:
    """
    Class for Dialer App ,finding and clicking elements inside the app.
    """
    def __init__(self,driver):
        """Initialize the CallerApp on Pixel7 with a WebDriver instance."""
        # Merge APP_Caller into capabilities_Pixel7 if APP_Caller contains additional capabilities
        capabilities = {**CAPABILITIES_PIXEL7, **APP_CALLER}
        self.driver = mobile.Remote(APPIUM_SERVER_URL_LOCAL, capabilities)


    def click_pad(self):
        pad_find = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'com.google.android.dialer:id/dialpad_fab')))
        pad_find.click()

    def find_dial_phone(self):
        dial = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'com.google.android.dialer:id/digits')))
        return dial

    def dial_input(self, number):
        dial = self.find_dial_phone().send_keys(number)
        return dial



    def call_phone(self):
        call = self.driver.find_element(AppiumBy.ID, 'com.google.android.dialer:id/dialpad_voice_call_button')
        return call

    def call_phone_click(self):
        self.call_phone().click()
    def hang_up_call(self):
        hang_up = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'com.google.android.dialer:id/incall_end_call')))
        return hang_up
    def hang_up_click(self):
        self.hang_up_call().click()
    def sms_click(self):
        send_message = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                        'new UiSelector().resourceId("com.google.android.dialer:id/search_action_text").text("Send a message")')))
        send_message.click()

    def message_input(self):
        message_input_draft = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'com.google.android.apps.messaging:id/compose_message_text')))
        return message_input_draft

    def message_input_sendkeys(self, draft_message):
        self.message_input().send_keys(draft_message)

    def find_send_icon(self):
        send_icon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//android.view.View[@resource-id="Compose:Draft:Send"]')))
        return send_icon

    def send_icon_click(self):
        self.find_send_icon().click()

    def get_dialed_number(self):
        dialed_number = self.find_dial_phone().text
        return dialed_number

    def get_inputted_message(self):
        input_field = self.message_input()
        return input_field.text
