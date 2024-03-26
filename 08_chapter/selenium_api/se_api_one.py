from selenium import webdriver
from selenium.webdriver.common.by import By


class Se:

    def __init__(self, timeout: float = 10):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(timeout)

    def open(self, url: str):
        self.driver.get(url)

    def close(self):
        self.driver.close()

    def by_id(self, elem: str):
        return self.driver.find_element(By.ID, elem)

    def by_name(self, elem: str):
        return self.driver.find_element(By.NAME, elem)
