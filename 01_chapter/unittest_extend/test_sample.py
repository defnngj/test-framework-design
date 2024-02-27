"""
test_sample.py
xtest 使用
"""
import xtest
from selenium import webdriver


class MyTest(xtest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.name = self.get_name

    def tearDown(self):
        self.driver.quit()

    def test_case(self):
        self.driver.get("https://www.baidu.com/")
        search_input = self.driver.find_element("id", "kw")
        search_input.send_keys(self.name)
        search_input.submit()
        self.sleep(2)
        result_title = self.driver.find_elements("css selector", "div > h3.c-title > a")
        for title in result_title:
            print(f"title: {title.text}")
            self.assert_in_text(self.name, title.text)


if __name__ == '__main__':
    xtest.run()
