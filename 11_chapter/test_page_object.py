from time import sleep
from selenium.webdriver import Chrome
from design_patterns.page_object import BingPage

driver = Chrome()
driver.get("https://cn.bing.com")

# 调用BingPage类
page = BingPage(driver)
page.search_input.send_keys("page object tests")
page.search_icon.click()

sleep(4)
driver.close()

