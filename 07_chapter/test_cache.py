import hashlib
import unittest
from time import time

from extends.cache import cache


def login(username: str, password: str) -> any:
    """
    模拟登录生成token
    """
    src = f'{username}.{password}'
    m = hashlib.md5()
    m.update(src.encode("utf-8"))
    token = m.hexdigest()

    token_value = cache.get("token")
    if token_value is None:
        cache.set({"token": token})

    return token


class CacheTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 清空缓存
        cache.clear()

    @classmethod
    def tearDownClass(cls):
        # 获取所有缓存
        all_token = cache.get()
        print(f"all: {all_token}")

    def setUp(self):
        self.start = time()

    def tearDown(self):
        end = time()
        print(f"run time:{end - self.start}")

    def test_case1(self):
        token = login("admin", "abc123")
        print(f"case1 token: {token}")

    def test_case2(self):
        token = login("admin", "abc123")
        print(f"case2 token: {token}")

    def test_case3(self):
        token = login("admin", "abc123")
        print(f"case3 token: {token}")


if __name__ == '__main__':
    unittest.main()
