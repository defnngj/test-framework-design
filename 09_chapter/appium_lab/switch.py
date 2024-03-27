# appium_lab/switch.py


class Switch:
    """
    基于appium 切换上下文
    """

    def __init__(self, driver):
        self.driver = driver

    def context(self) -> str:
        """
        返回当前context.
        :return
        """
        current_context = self.driver.current_context
        all_context = self.driver.contexts
        print(f"current context: {current_context}.")
        print(f"all context: {all_context}.")
        return current_context

    def switch_to_app(self) -> None:
        """
        切换到原生app.
        """
        current_context = self.driver.current_context
        if current_context != "NATIVE_APP":
            print("Switch to native.")
            self.driver.switch_to.context('NATIVE_APP')

    def switch_to_web(self, context_name: str = None) -> None:
        """
        切换到webview.
        :param context_name: webview 上下文名称
        :return
        """
        print("Switch to webview.")
        if context_name is not None:
            self.driver.switch_to.context(context_name)
        else:
            all_context = self.driver.contexts
            for context in all_context:
                if "WEBVIEW" in context:
                    self.driver.switch_to.context(context)
                    break
            else:
                raise NameError("No WebView found.")

    def switch_to_flutter(self) -> None:
        """
        切换到flutter.
        :return
        """
        current_context = self.driver.current_context
        if current_context != "FLUTTER":
            print("Switch to flutter.")
            self.driver.switch_to.context('FLUTTER')
