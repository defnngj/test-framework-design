from selenium_api.se_api_four import Se

he = Se()
he.open("https://www.baidu.com").type(name="wd", text="selenium").click(id="su").close()
