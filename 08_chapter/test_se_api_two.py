from selenium_api.se_api_two import Se

two = Se()
two.open("https://www.baidu.com")
two.type(name="wd", text="selenium", enter=True)
two.close()

import itertools

itertools.product()
