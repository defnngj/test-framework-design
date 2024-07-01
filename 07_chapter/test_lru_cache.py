import hashlib
import unittest
from functools import lru_cache
from time import time


@lru_cache(maxsize=None)
def login(username: str, password: str) -> any:
    """
    模拟登录生成token
    """
    src = f'{username}.{password}'
    m = hashlib.md5()
    m.update(src.encode("utf-8"))
    token = m.hexdigest()
    return token


class CacheTest(unittest.TestCase):

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
