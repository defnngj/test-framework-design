# bot_style.py
from selenium.webdriver.remote.webdriver import WebDriver


class ActionBot:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click(self, *locator, times=1):
        """
        点击
        :param locator: 元素定位
        :param times: 点击次数
        :return:
        """
        elem = self.driver.find_element(*locator)
        for _ in range(times):
            elem.click()

    def type(self, *locator, text):
        """
        输入
        :param locator: 元素定位
        :param text: 输入文本
        :return:
        """
        elem = self.driver.find_element(*locator)
        elem.clear()
        elem.send_keys(text)
