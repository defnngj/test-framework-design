# page_object.py
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BingPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @property
    def search_input(self):
        return self.driver.find_element(By.ID, "sb_form_q")

    @property
    def search_icon(self):
        return self.driver.find_element(By.ID, "search_icon")
