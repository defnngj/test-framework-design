from selenium import webdriver

from page_object_lib.poium_page import BingPage

driver = webdriver.Chrome()
driver.get("https://cn.bing.com")

bp = BingPage(driver)
bp.search_input.send_keys("poium")
bp.search_icon.click()
bp.sleep(2)

result = bp.search_result
for r in result:
    print("搜索结果：", r.text)
