# appium_lab/find.py
from time import sleep

from appium.webdriver.common.appiumby import AppiumBy

from appium_lab.switch import Switch


class FindByText(Switch):
    """
    基于文本查找元素
    """

    def __find(self, class_name: str, attribute: str, text: str):
        """
        查找元素
        :param class_name: class名字
        :param attribute: 属性
        :param text: 文本
        """
        elems = self.driver.find_elements(AppiumBy.CLASS_NAME, class_name)
        for _ in range(3):
            if len(elems) > 0:
                break
            sleep(1)

        for elem in elems:
            if elem.get_attribute(attribute) is None:
                continue
            attribute_text = elem.get_attribute(attribute)
            if text in attribute_text:
                print(f'find -> {attribute_text}')
                return elem
        return None

    def find_text_view(self, text: str) -> None:
        """
        Android: 基于TextView查找文本
        :param text: 文本名
        """
        self.switch_to_app()
        for _ in range(3):
            elem = self.__find(class_name="android.widget.TextView",
                               attribute="text", text=text)
            if elem is not None:
                break
            sleep(1)
        else:
            raise ValueError(f"Unable to find -> {text}")

        return elem

    def find_text_field(self, text: str) -> None:
        """
        iOS: 基于XCUIElementTypeTextField查找文本
        :param text: 文本名
        """
        self.switch_to_app()
        for _ in range(3):
            elem = self.__find(class_name="XCUIElementTypeTextField",
                               attribute="name", text=text)
            if elem is not None:
                break
            sleep(1)
        else:
            raise ValueError(f"Unable to find -> {text}")
