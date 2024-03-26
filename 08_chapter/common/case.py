import unittest
from urllib.parse import unquote
from selenium import webdriver
from selenium.webdriver.common.by import By


# 定义浏览器驱动
class Browser:
    driver = None


# 定义unittest主方法
main = unittest.main

# 定位类型
LOCATOR_LIST = {
    'id': By.ID,
    'name': By.NAME,
    'xpath': By.XPATH,
    'css': By.CSS_SELECTOR,
    # ...
}


class TestCase(unittest.TestCase):
    """
    定义unittest测试类，实现断言方法
    """

    @classmethod
    def setUpClass(cls):
        """
        测试类初始化浏览器驱动
        """
        Browser.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        """
        测试类关闭浏览器
        """
        Browser.driver.close()

    @staticmethod
    def _get_element(**kwargs):
        by, value = next(iter(kwargs.items()))
        se_by = LOCATOR_LIST.get(by, None)
        if se_by is None:
            raise NameError("仅支持id/name/xpath/css定位，暂不支持其他定位方式")
        return Browser.driver.find_element(se_by, value)

    @staticmethod
    def open(url):
        """
        打开URL

        用法:
            self.open(url)
        """
        Browser.driver.get(url)

    def assertTitle(self, title: str = None, msg: str = None) -> None:
        """
        断言当前页面标题是否等于title.

        用法:
            self.assertTitle("title")
        """
        if title is None:
            raise AssertionError("断言的title不能为空.")

        print(f"assertTitle -> {title}.")
        self.assertEqual(title, Browser.driver.title, msg=msg)

    def assertInTitle(self, title: str = None, msg: str = None) -> None:
        """
        断言当前页面标题是否包含title.

        用法:
            self.assertTitle("title")
        """
        if title is None:
            raise AssertionError("断言的title不能为空.")

        print(f"assertInTitle -> {title}.")
        self.assertIn(title, Browser.driver.title, msg=msg)

    def assertUrl(self, url: str = None, msg: str = None) -> None:
        """
        判断当前页面地址是否为url.

        用法:
            self.assertUrl("url")
        """
        if url is None:
            raise AssertionError("断言的url不能为空.")

        print(f"assertUrl -> {url}.")
        current_url = unquote(Browser.driver.current_url)
        self.assertEqual(url, current_url, msg=msg)

    def assertInText(self, text: str = None, msg: str = None) -> None:
        """
        断言页面是否包含 text 文本.

        用法:
            self.assertInText("text")
        """
        if text is None:
            raise AssertionError("断言的text不能为空.")

        elem = Browser.driver.find_element(By.TAG_NAME, "html")
        print(f"assertText -> {text}.")
        self.assertIn(text, elem.text, msg=msg)

    def assertElement(self, **kwargs) -> None:
        """
        断言页面定位元素是否存在.

        用法:
            self.assertElement(css="#id")
        """
        try:
            self._get_element(**kwargs)
            elem = True
        except Exception as e:
            print("assertElement error", e)
            elem = False
        print(f"assertElement.")
        self.assertTrue(elem)
