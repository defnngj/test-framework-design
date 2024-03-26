from selenium_api.se_api_three import *

start_chrome()
go_to("http://www.baidu.com")
wirte(name("wd"), text="selenium")
click(id("su"))
close()
