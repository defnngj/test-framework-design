import hashlib
import unittest
from random import randint

import requests

from tools.dependence import dependent_func, redis_client


class DependentTest(unittest.TestCase):

    @staticmethod
    def user_login(username, password):
        """
        模拟用户登录，获取登录token
        """
        src = username + password
        m = hashlib.md5()
        m.update(src.encode())
        md5_str = m.hexdigest()
        print(f"生成token: {md5_str}")
        return md5_str

    @staticmethod
    @dependent_func(user_login, username="tom", password="t123")
    def get_project():
        """
        基于登录token，模拟查询项目ID
        """
        token = redis_client.get("user_login")
        print(f"获取token: {token}, 调用项目查询ID接口")
        pid = randint(1, 100)
        print(f"生成项目ID: {pid}")
        return pid

    @dependent_func(get_project, key_name="pid")
    def test_case(self):
        """
        测试用例，基于项目ID创建模块
        """
        pid = redis_client.get("pid")
        payload = {"pid": pid, "module_name": "module name"}
        r = requests.post("https://httpbin.org/post", data=payload)
        print(r.text)


if __name__ == '__main__':
    unittest.main()
