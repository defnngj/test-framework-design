import hashlib
import unittest
from time import time
from functools import lru_cache


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

    def test_case1(self):
        start = time()
        token = login("admin", "abc123")
        end = time()
        print(f"case1 token: {token}, run time:{ end - start}")

    def test_case2(self):
        start = time()
        token = login("admin", "abc123")
        end = time()
        print(f"case2 token: {token}, run time:{ end - start}")

    def test_case3(self):
        start = time()
        token = login("admin", "abc123")
        end = time()
        print(f"case3 token: {token}, run time:{ end - start}")


if __name__ == '__main__':
    unittest.main()
