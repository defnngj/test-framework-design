from appium import webdriver
from appium.options.android import UiAutomator2Options
from page_object_lib.poium_page import CalculatorPage


capabilities = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    'appPackage': 'com.huawei.calculator',
    'appActivity': '.Calculator',
}
options = UiAutomator2Options().load_capabilities(capabilities)
driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

page = CalculatorPage(driver)
page.number_1.click()
page.add.click()
page.number_2.click()
page.eq.click()
