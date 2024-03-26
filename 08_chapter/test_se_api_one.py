from selenium_api.se_api_one import Se

one = Se()
one.open("https://www.baidu.com")
one.by_name("wd").send_keys("selenium")
one.by_id("su").click()
one.close()
