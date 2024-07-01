from selenium import webdriver
from selenium.webdriver.common.by import By


dr = webdriver.Chrome()
dr.get("https://www.baidu.com")

dr.find_element(By.ID, "kw").send_keys("selenium")
dr.find_element(By.ID, "su").click()

dr.quit()
