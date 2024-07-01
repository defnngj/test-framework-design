# appium_android_demo.py
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# 定义元素
elems = {
    "search_icon": "com.meizu.flyme.flymebbs:id/view_search",
    "search_input": "com.meizu.flyme.flymebbs:id/et_search",
    "result_title": '//android.widget.TextView[@resource-id="com.meizu.flyme.flymebbs:id/tv_post_title"]'
}

# Android App配置
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
driver.implicitly_wait(5)

# 搜索 "flyme" 关键字
driver.find_element("id", elems.get("search_icon")).click()
driver.find_element("id", elems.get("search_input")).send_keys("flyme")
driver.execute_script('mobile: performEditorAction', {'action': 'search'})

# 打印结果列表
result_list = driver.find_elements(AppiumBy.XPATH, elems.get("result_title"))
for title in result_list:
    print(title.text)

# 关闭App
driver.quit()
