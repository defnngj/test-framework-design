# se_api_two.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 定义定位方法对应字典
LOCATOR_LIST = {
    'id': By.ID,
    'name': By.NAME,
    # ...
}


class Se:

    def __init__(self, timeout: float = 10):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(timeout)

    def open(self, url: str):
        self.driver.get(url)

    def close(self):
        self.driver.close()

    def get_element(self, **kwargs):
        by, value = next(iter(kwargs.items()))
        se_by = LOCATOR_LIST.get(by, None)
        if se_by is None:
            raise NameError("仅支持id/name定位，暂不支持其他定位方式")
        return self.driver.find_element(se_by, value)

    def type(self, text: str, clear: bool = False, enter: bool = False, **kwargs):
        elem = self.get_element(**kwargs)
        if clear:
            elem.send_keys(text)
        elem.send_keys(text)
        if enter:
            elem.send_keys(Keys.ENTER)

    def click(self, **kwargs):
        elem = self.get_element(**kwargs)
        elem.click()
