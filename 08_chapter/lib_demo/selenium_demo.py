# selenium_demo.py
from selenium import webdriver
from selenium.webdriver.common.by import By

# Chrome/Firefox浏览器
# browser = webdriver.Chrome()
browser = webdriver.Firefox()

browser.get('http://selenium.dev/')

assert browser.title == "Selenium"

browser.find_element(By.PARTIAL_LINK_TEXT, "x")
