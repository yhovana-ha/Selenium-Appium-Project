"""
Globals Variables for NikeAppium Project this file includes the Capabilities of pixel 7
The urls for the websites use in the tests and the capabilities for each app that was used.
"""

CAPABILITIES_PIXEL7 = dict(
    platformName='Android',
    deviceName='Pixel7',
    udid="emulator-5554",
    platformVersion="35",
    automationName= "UiAutomator2",
    newCommandTimeout= 120,
    language='en',
    locale='US'
)
NIKE_URL = "https://www.nike.com"
WISE_URL = "https://wise.com/gb/currency-converter/usd-to-ils-rate"
APPIUM_SERVER_URL_LOCAL = 'http://localhost:4723/wd/hub'
APP_CALCULATOR= dict(
    appActivity='com.android.calculator2.Calculator',
    appPackage='com.google.android.calculator',
)
APP_CALLER = dict(
    appPackage='com.google.android.dialer',
    appActivity='.extensions.GoogleDialtactsActivity'
)
APP_GOOGLE_MAPS = dict(
    appPackage='com.google.android.apps.maps',
    appActivity='com.google.android.maps.MapsActivity'
)
