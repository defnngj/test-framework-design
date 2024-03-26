# selenium_demo.py
from selenium import webdriver

# Chrome/Firefox浏览器
# browser = webdriver.Chrome()
browser = webdriver.Firefox()

browser.get('http://selenium.dev/')

assert browser.title == "Selenium"
