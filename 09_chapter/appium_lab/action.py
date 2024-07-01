# appium_lab/action.py
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from appium_lab.switch import Switch


class Action(Switch):
    """
    封装基本动作: 滑动、触摸等
    """

    def __init__(self, driver):
        Switch.__init__(self, driver)
        self.switch_to_app()
        self._size = self.driver.get_window_size()
        self.width = self._size.get("width")
        self.height = self._size.get("height")

    def size(self) -> dict:
        """
        返回屏幕尺寸
        """
        print(f"screen resolution: {self._size}")
        return self._size

    def tap(self, x: int, y: int) -> None:
        """
        触摸坐标位
        :param x: x 坐标
        :param y: y 坐标
        :return:
        """
        self.switch_to_app()
        print(f"top x={x},y={y}.")
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(
            self.driver,
            mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(x, y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        sleep(2)

    def swipe_up(self, times: int = 1, upper: bool = False) -> None:
        """
        向上滑动
        :param times: 滑动次数，默认1
        :param upper: 由于屏幕键盘遮挡，可以选择滑动上半部分。
        :return:
        """
        self.switch_to_app()
        print(f"swipe up {times} times")
        x_start = int(self.width / 2)
        x_end = int(self.width / 2)

        if upper is True:
            self.height = (self.height / 2)

        y_start = int((self.height / 3) * 2)
        y_end = int((self.height / 3) * 1)

        for _ in range(times):
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(
                self.driver,
                mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(x_start, y_start)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(x_end, y_end)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            sleep(1)

    def swipe_down(self, times: int = 1, upper: bool = False) -> None:
        """
        向下滑动
        :param times: 滑动次数，默认1
        :param upper: 由于屏幕键盘遮挡，可以选择滑动上半部分。
        :return:
        """
        self.switch_to_app()
        print(f"swipe down {times} times")
        x_start = int(self.width / 2)
        x_end = int(self.width / 2)

        if upper is True:
            self.height = (self.height / 2)

        y_start = int((self.height / 3) * 1)
        y_end = int((self.height / 3) * 2)

        for _ in range(times):
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(
                self.driver,
                mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(x_start, y_start)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(x_end, y_end)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            sleep(1)
