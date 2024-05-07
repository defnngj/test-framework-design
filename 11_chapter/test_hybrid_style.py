from time import sleep
from selenium.webdriver import Chrome
from design_patterns.hybrid_style import BingPage

driver = Chrome()
driver.get("http://cn.bing.com")

# 调用BingPage类
page = BingPage(driver)
page.search_input(text="bot style tests", enter=True)

sleep(4)
driver.close()

