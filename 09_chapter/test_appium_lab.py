from time import sleep
from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from appium_lab.switch import Switch
from appium_lab.action import Action
from appium_lab.find import FindByText
from appium_lab.keyevent import KeyEvent

capabilities = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "appPackage": "com.meizu.flyme.flymebbs",
    "appActivity": "com.meizu.myplus.ui.splash.SplashActivity",
    "noReset": True,
}

appium_server_url = "http://127.0.0.1:4723"

options = UiAutomator2Options().load_capabilities(capabilities)
driver = Remote(command_executor=appium_server_url, options=options)
driver.implicitly_wait(10)

# 点击输入框，调起屏幕键盘
driver.find_element(AppiumBy.ID, "com.meizu.flyme.flymebbs:id/view_search").click()

# 键盘输入
key = KeyEvent(driver)
key.key_text("Flyme10")
sleep(1)
key.press_key("ENTER")

# 使用文本定位
find = FindByText(driver)
find.find_text_view("综合讨论").click()
sleep(5)

# 滑动&点击操作
action = Action(driver)
# 屏幕尺寸
action.size()
# 向上滑动
action.swipe_up(times=3)
# 向下滑动
action.swipe_down(times=1)
# 触摸坐标位
action.tap(x=100, y=1333)

# 上下文切换
context = Switch(driver)
# 打印并返回当前上下文
context.context()
# 切换到 webview
context.switch_to_web()
# 切换到 native
context.switch_to_app()
# 切换到 flutter
context.switch_to_flutter()
