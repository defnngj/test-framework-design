# appium_orc_demo.py
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from extension.ocr_extension import OCRCommand


capabilities = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "appPackage": "com.meizu.flyme.flymebbs",
    "appActivity": "com.meizu.myplus.ui.splash.SplashActivity",
    "noReset": True,
}

appium_server_url = "http://127.0.0.1:4723"
options = UiAutomator2Options().load_capabilities(capabilities)
driver = webdriver.Remote(command_executor=appium_server_url, options=options, extensions=[OCRCommand])
driver.implicitly_wait(10)

ocr = driver.ocr_command({})
print(ocr)

driver.switch_to.context('OCR')
element = driver.find_element(AppiumBy.XPATH, '//words/item[text() = "Flyme"]')
# 点击
element.click()

# 是否显示
print(element.is_displayed())

# 尺寸
print(element.size)

# 位置
print(element.location)

# 坐标&尺寸
print(element.rect)

# 文本
print(element.text)

# 属性（仅支持 confidence）
print(element.get_attribute("confidence"))







