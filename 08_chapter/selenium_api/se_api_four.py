import time
from selenium import webdriver
from selenium.webdriver.common.by import By

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
        return self

    def close(self):
        self.driver.close()
        return self

    def get_element(self, **kwargs):
        by, value = next(iter(kwargs.items()))
        se_by = LOCATOR_LIST.get(by, None)
        if se_by is None:
            raise NameError("仅支持id/name定位，暂不支持其他定位方式")
        return self.driver.find_element(se_by, value)

    def sleep(self, sec):
        time.sleep(sec)
        return self

    def type(self, text: str, **kwargs):
        elem = self.get_element(**kwargs)
        elem.send_keys(text)
        return self

    def click(self, **kwargs):
        elem = self.get_element(**kwargs)
        elem.click()
        return self
