# appium_image_demo.py
import os
import base64
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


capabilities = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "appPackage": "com.meizu.flyme.flymebbs",
    "appActivity": "com.meizu.myplus.ui.splash.SplashActivity",
    "noReset": True,
}

appium_server_url = "http://127.0.0.1:4723"
options = UiAutomator2Options().load_capabilities(capabilities)
driver = webdriver.Remote(command_executor=appium_server_url, options=options)

driver.update_settings({"fixImageTemplatescale": True})
driver.implicitly_wait(10)

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "image", "phone.jpg")

with open(image_path, 'rb') as png_file:
    b64_data = base64.b64encode(png_file.read()).decode('UTF-8')

driver.find_element(AppiumBy.IMAGE, b64_data).click()
