from selenium import webdriver

from page_object_lib.spf_page import BingPage

driver = webdriver.Chrome()
driver.get("https://cn.bing.com")

bp = BingPage(driver)
bp.search("selenium-page-factory")

driver.quit()
