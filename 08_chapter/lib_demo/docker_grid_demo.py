# docker_grid_demo.py
from selenium import webdriver
from selenium.webdriver import Remote

# Firefox浏览器配置
ffOptions = webdriver.FirefoxOptions()
driver = Remote(command_executor='http://localhost:4444/wd/hub',
                options=ffOptions)

driver.get("https://www.bing.com")
search = driver.find_element("id", "sb_form_q")
search.send_keys("docker-selenium")
search.submit()
