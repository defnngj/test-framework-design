from applitools.selenium import Eyes, Target, Configuration
from selenium import webdriver
from selenium.webdriver.common.by import By

# 初始化 Selenium WebDriver
driver = webdriver.Chrome()

# 初始化 Applitools Eyes
eyes = Eyes()
eyes.api_key = "{api key}"

try:
    # 创建一个新的测试实例配置, 全局
    config = Configuration()
    config.app_name = 'Applitools Hello World Demo'
    config.test_name = 'Hello World Test with Links and Button'

    # 开始视觉测试
    with eyes.open(
            driver, app_name="Hello World App",
            test_name="Hello World Test",
            viewport_size={'width': 800, 'height': 600}):

        # 访问目标页面
        driver.get("https://applitools.com/helloworld")

        # 检查主页面
        eyes.check("Main Page", Target.window())

        # 点击第一个 diff 链接
        driver.find_element(By.CSS_SELECTOR, 'a[href="?diff1"]').click()
        eyes.check("Diff1 Page", Target.window())

        # 返回主页面
        driver.back()

        # 点击第二个 diff 链接
        driver.find_element(By.CSS_SELECTOR, 'a[href="?diff2"]').click()
        eyes.check("Diff2 Page", Target.window())

        # 返回主页面
        driver.back()

        # 点击按钮
        driver.find_element(By.TAG_NAME, 'button').click()

        # 检查按钮点击后的页面
        eyes.check("After Button Click", Target.window())

        # 结束视觉测试并关闭浏览器
        eyes.close()
finally:
    driver.quit()
    eyes.abort()
