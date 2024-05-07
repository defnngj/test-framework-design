# poium_core/page.py


class Page:
    """
    定义Page类
    """

    def __init__(self, driver):
        self.driver = driver


class Element:
    """
    定义 Element 类
    """

    def __init__(self, *locator):
        if len(locator) < 1:
            raise ValueError("Please specify only one locator")
        self.locator = locator

    def __get__(self, instance, owner):
        if instance is None:
            return None
        self.driver = instance.driver
        return self

    def input(self, text: str):
        """
        input 输入
        :param text:
        """
        self.driver.find_element(*self.locator).send_keys(text)

    def click(self):
        """
        click 点击
        """
        self.driver.find_element(*self.locator).click()
