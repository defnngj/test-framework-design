import unittest
from selenium.webdriver import Chrome


class MyTest(unittest.TestCase):

    def test_case(self):
        driver = Chrome()
        driver.get("https://www.selenium.dev/")
        # 获取当前页面URL，进行断言
        current_title = driver.title
        self.assertEqual(current_title, "Selenium")


if __name__ == '__main__':
    unittest.main()
