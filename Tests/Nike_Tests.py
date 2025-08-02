from unittest import TestCase
from selenium.webdriver.edge.service import Service
from appium import webdriver as mobile
from selenium import webdriver as web
from WebPages.Wise_Page import WiseExchangeRate
from WebPages.Nike_CategoryPage import NikeCategoryPage
from globals import CAPABILITIES_PIXEL7,NIKE_URL,APPIUM_SERVER_URL_LOCAL
from WebPages.Nike_HomePage import NikeHomePage
from WebPages.Nike_RetailPage import NikeRetailPage
from WebPages.Nike_StorePage import  NikeStorePage
from WebPages.Nike_ProductPage import NikeProductPage
from AppPages.Caller_App import CallerAppPage
from AppPages.Map_App import MapAppPage
from AppPages.Calc_APP import CalcAppPage
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")

class NikeTests(TestCase):
    def setUp(self):
        """Set up the test environment."""
        service = Service(executable_path='path/to/edgedriver')
        self.driver = web.Edge(service=service)
        self.driver.get(NIKE_URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver_mobile = mobile.Remote(APPIUM_SERVER_URL_LOCAL, CAPABILITIES_PIXEL7)
        # Initialize page objects for various site components
        self.home_page = NikeHomePage(self.driver)
        self.category = NikeCategoryPage(self.driver)
        self.store_page = NikeStorePage(self.driver)
        self.store_location = NikeRetailPage(self.driver)
        self.product_page = NikeProductPage(self.driver)
        self.wise_page = WiseExchangeRate(self.driver)

    def tearDown(self):
        self.driver.quit()
        self.driver_mobile.quit()

    def test_call_store(self):
        """ Test: Go to Nike website,
            go to find store section search a Nike location,
            find the phone number and call the store.
        """
        # Initialize Appium driver
        self.caller_app = CallerAppPage(self.driver_mobile)
        # Calling the Helper function choose_store_number_func
        phone_number = self.choose_store_number_func()
        self.assertIsNotNone(phone_number, "Phone number should not be None")
        self.assertTrue(phone_number.strip(), "Phone number should not be empty")
        # Open the dialer and input the phone number
        self.caller_app.click_pad()
        self.caller_app.dial_input(phone_number)

        # Assert that the phone number on the digit pad matches the expected phone number
        dialed_number = self.caller_app.get_dialed_number()
        self.assertEqual(phone_number, dialed_number, "Dialed phone number does not match the expected phone number.")

        # Call the number of the store
        self.caller_app.call_phone_click()
        # Hang up the call
        self.caller_app.hang_up_click()

    def test_get_directions(self):
        """ Test: Go to Nike website ,
            go to find store section search a nike location
            find the store address and search directions in maps.
        """
        #Initialize Map App
        self.map_app = MapAppPage(self.driver_mobile)
        # Calling the Helper function choose_store_address_func
        address = self.choose_store_address_func()
        #Testing Phone
        self.map_app.touch_skip_start()
        self.map_app.click_address()
        self.map_app.send_keys_search_address(address)
        self.map_app.located_address().click()
        address_parts = address.split('\n')
        extracted_address = address_parts[1] if len(address_parts) > 1 else ""
        # Extract the relevant part of the checked location
        checked_location_text = self.map_app.checked_location()
        checked_location_parts = checked_location_text.split('\n')
        extracted_checked_location_text = checked_location_parts[1] if len(checked_location_parts) > 1 else ""
        self.assertEqual(extracted_checked_location_text, checked_location_text)

    def test_sms_store(self):
        """ Test: Go to Nike website,
            go to find store section search a Nike location,
            find the phone number and SMS message the store.
        """
        # Initialize Appium driver
        self.caller_app = CallerAppPage(self.driver_mobile)
        # Calling the Helper function choose_store_number_func
        phone_number = self.choose_store_number_func()

        # Open the dialer and input the phone number
        self.caller_app.click_pad()
        self.caller_app.dial_input(phone_number)

        # Assert that the phone number on the dialer is correct
        dialed_number = self.caller_app.get_dialed_number()
        self.assertEqual(phone_number, dialed_number, "Dialed phone number does not match the expected phone number.")

        # Send SMS to the store
        self.caller_app.sms_click()
        # Input the message to the store
        message = "Hello, can you please check on my order? ID: 315635250"
        self.caller_app.message_input_sendkeys(message)

        # Retrieve and assert the SMS message
        sent_message = self.caller_app.get_inputted_message()
        self.assertEqual(message, sent_message, "The SMS message does not match the expected message.")

        # Click send
        logging.info(f"The store has received your message: {message}")
        self.caller_app.send_icon_click()

    def test_product_price_exchange(self):
        """ Test: Go to Nike website,
            search a product in men category, get the price and exchange it to dollars.
        """
        self.calc_app = CalcAppPage(self.driver_mobile)
        # Go to men category > shoes > jordan
        self.home_page.men_page_click()
        self.category.shoes_page_click()
        self.category.jordan_click()

        # Choose 1 product, get the name and the price
        self.product_page.first_product_click()
        product_name = self.product_page.get_product_name()
        product_price_shekel = self.product_page.get_product_price()
        logging.info(f"Product: {product_name}, Price: {product_price_shekel} ILS")

        # Open a new tab and use WiseExchangeRate class to get the conversion rate
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        wise_exchange = WiseExchangeRate(self.driver)
        wise_exchange.open_wise()
        conversion_rate = wise_exchange.get_exchange_rate()
        logging.info(f"Conversion Rate: 1 USD = {conversion_rate} ILS")

        # Close the new tab and switch back to the original tab
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        # Calculate the price in dollars using the calculator app
        self.calc_app.clear_input_indicator()

        # Enter the product price in shekels
        for digit in str(product_price_shekel):
            self.calc_app.input_digit(digit)

        # Enter the division operator
        self.calc_app.click_operator_divide()

        # Enter the conversion rate
        for digit in str(conversion_rate):
            self.calc_app.input_digit(digit)

        # Perform the calculation
        self.calc_app.click_operator_equal()

        # Get the calculation result
        result = self.calc_app.get_result()
        logging.info(f"Calculation Result: {result} USD")

        # Perform the assertion
        expected_price_usd = product_price_shekel / conversion_rate
        self.assertAlmostEqual(float(result), expected_price_usd)


    def test_calc_2_products_price(self):
        """ Test: Go to Nike website,
            search a product in men category, get the price and exchange it to dollars.
        """
        self.calc_app = CalcAppPage(self.driver_mobile)
        # Go to men category > shoes > jordan
        self.home_page.men_page_click()
        self.category.shoes_page_click()
        self.category.jordan_click()

        # Choose the first product, get the name and the price
        self.product_page.choose_first_product()
        self.product_page.first_product_click()
        first_product_name = self.product_page.get_product_name()
        first_product_price = self.product_page.get_product_price()
        logging.info(f"First Product: {first_product_name}, Price: {first_product_price}")

        # Navigate back to the product listing page
        self.driver.back()
        # Choose the second product, get the name and the price
        self.product_page.choose_second_product()
        self.product_page.second_product_click()
        second_product_name = self.product_page.get_product_name()
        second_product_price = self.product_page.get_product_price()
        logging.info(f"Second Product: {second_product_name}, Price: {second_product_price}")

        # Open Calc App and enter the first item price
        self.calc_app.input_field_sendkeys(first_product_price)

        # Click the plus operator
        self.calc_app.click_operator_plus()

        # Enter the second item price
        self.calc_app.input_field_sendkeys(second_product_price)

        # Click the equals operator
        self.calc_app.click_operator_equal()

        # Get the calculation result
        result = self.calc_app.get_result()
        logging.info(f"Calculation Result: {result}")

        # Check if the result is correct
        expected_result = first_product_price + second_product_price
        self.assertAlmostEquals(str(expected_result), result)

    def choose_store_number_func(self):
        self.home_page.find_store_click()
        self.store_location.first_store_click()
        self.store_location.first_store_click()
        store_status = self.store_page.store_status()
        phone_number = self.store_page.store_phone_number()
        if store_status == "Open":
            logging.info(f"The store is open. Phone number: {phone_number}")
        else:
            logging.info("The store is closed.")

        return phone_number

    def choose_store_address_func(self):
        self.home_page.find_store_click()
        self.store_location.first_store_click()
        self.store_location.first_store_click()

        store_status = self.store_page.store_status()
        phone_number = self.store_page.store_phone_number()
        address = self.store_page.store_address()
        if store_status == "Open":
            logging.info(f"The store is open. Phone number: {phone_number}")

            # Retrieve the address
            logging.info(f"The store address is: {address}")
        else :
            logging.info("The store is closed.")
        return address