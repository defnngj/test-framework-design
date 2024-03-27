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

driver.update_settings({"getMatchedImageResult": True})
driver.update_settings({"fixImageTemplatescale": True})
driver.implicitly_wait(10)

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "image", "phone.jpg")

with open(image_path, 'rb') as png_file:
    b64_data = base64.b64encode(png_file.read()).decode('UTF-8')

# driver.find_element(AppiumBy.IMAGE, b64_data).click()

# 元素操作
element = driver.find_element(AppiumBy.IMAGE, b64_data)

# 点击
element.click()

# 是否显示
print(element.is_displayed())

# 获取尺寸
print(element.size)

# 元素在可渲染画布中的位置
print(element.location)

# 获取元素相对于视图的位置
print(element.location_in_view)

# 获取坐标&尺寸
print(element.rect)

# 返回匹配的图像作为base64数据, 需要设置 getMatchedImageResult为true
print(element.get_attribute("visual"))

# 自Appium 1.18.0起，返回相似度分数为浮点数，范围在[0.0, 1.0]之间。
print(element.get_attribute("score"))





