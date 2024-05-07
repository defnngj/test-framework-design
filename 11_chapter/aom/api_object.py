import requests


class OrderAPIObject:

    def add_item_to_cart(self, item_id):
        """
        发出API请求和向购物车添加商品
        :param item_id:
        :return:
        """
        ...

    def set_shipping_details(self, details):
        """
        通过API请求设置收件信息
        :param details:
        :return:
        """
        ...

    def place_order(self):
        """
        下订单并接收确认
        :return:
        """
        ...


class OrderAPIObject:

    def __init__(self):
        # 调用前置方法
        self.prepare_order()

    def prepare_order(self):
        """
        准备下订单所需的前置工作
        :return:
        """
        ...

    def place_order(self) -> dict:
        """
        下订单，以及处理错误响应
        :return: OrderConfirmation ErrorResponse
        """
        try:
            resp = requests.get('http://example.com', timeout=1)
            resp.raise_for_status()
            print(resp.text)
        except requests.exceptions.Timeout as e:
            print(f"请求超时: {e}")
        except requests.exceptions.RequestException as e:
            print(f"发生了请求异常: {e}")


class UserAPIObject:

    def register_one(self, name: str, email: str, password: str):
        """
        实现用户注册API
        :param name:
        :param email:
        :param password:
        :return:
        """
        ...

    def register_two(self, user: dict):
        """
        实现用户注册API
        :param user:
        :return:
        """
        name = user.get("name", "")
        email = user.get("email", "")
        password = user.get("password", "")
        ...
