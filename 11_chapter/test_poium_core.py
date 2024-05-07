from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from poium_core.page import Page, Element


class BingPage(Page):
    """bing页面元素"""
    search_input = Element(By.ID, "sb_form_q")
    search_icon = Element(By.ID, "search_icon")


if __name__ == '__main__':
    driver = Chrome()
    driver.get("https://cn.bing.com")

    bp = BingPage(driver)
    bp.search_input.input("poium")
    bp.search_icon.click()
