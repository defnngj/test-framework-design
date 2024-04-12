import json

import requests


class UserLogin:
    """
    用户登录封装类
    """

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_token(self):
        """
        获取用户登录token
        """
        url = "http://httpbin.org/post"

        data = {
            "username": self.username,
            "password": self.password,
            "token": "token123"  # << 假装这是接口返回的toKen
        }
        r = requests.post(url, data=data)

        if r.status_code != 200:
            raise ValueError("接口请求失败")

        try:
            r.json()
        except json.decoder.JSONDecodeError:
            raise ValueError("接口不是JSON格式")

        if r.json()["headers"]["Host"] != "httpbin.org":
            raise ValueError("接口返回必要参数错误")

        user_token = r.json()["form"]["token"]

        return user_token


if __name__ == '__main__':
    login = UserLogin("admin", "abc123")
    token = login.get_token()
    print(f"get token: {token}")
