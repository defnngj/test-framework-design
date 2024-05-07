# shop_object.py
from random import randint
import json
import requests


BASE_URL = "https://httpbin.org"

class AuthAPIObject:

    def __init__(self, api_key):
        self.api_key = api_key

    def get_token(self, user_id:str) -> str:
        """
        模拟：根据用户ID生成登录token
        :param user_id:
        :return:
        """
        data = {"user_id": user_id, "token": "t" + str(randint(10000, 99999))}
        resp = requests.post(BASE_URL + "/post?key=" + self.api_key, data=data).json()
        return resp["form"]["token"]


class UserAPIObject:

    def __init__(self, token: str):
        self.token = token

    def get_user_data(self, user_id: str):
        """
        模拟：根据用户ID查询用户信息
        :param user_id:
        :return:
        """
        headers = {"token": self.token}
        params = {"user_id": user_id, "name": "tom", "email": "tom@gmail.com", "age": 23}
        resp = requests.post(BASE_URL + "/post", headers=headers, json=params).json()
        return json.loads(resp["data"])


class ProductAPIObject:

    def __init__(self, token: str):
        self.token = token

    def get_product_data(self, product_id: str):
        """
        模拟：根据产品ID查询产品信息
        :param product_id:
        :return:
        """
        headers = {"token": self.token}
        params = {"product_id": product_id, "name": "潮流T恤", "type": "衣服", "price": 69.9}
        resp = requests.post(BASE_URL + "/post", headers=headers, json=params).json()
        return json.loads(resp["data"])



if __name__ == '__main__':
    auth_api = AuthAPIObject("api_key_123")
    login_token = auth_api.get_token("123")
    user_api = UserAPIObject(login_token)
    # product_api = ProductAPIObject(login_token)
    user_info = user_api.get_user_data("tom123")
    # product_info = product_api.get_product_data("p123")
    print(type(user_info))
    # print(product_info)


