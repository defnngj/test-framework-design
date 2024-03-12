import hashlib
import unittest
from time import time
import redis

redis_client = redis.Redis()

def login(username: str, password: str) -> any:
    """
    模拟登录生成token
    """
    global redis_client
    token = redis_client.get(username)
    # 如果有token 直接返回
    if token is not None:
        return token

    src = f'{username}.{password}'
    m = hashlib.md5()
    m.update(src.encode("utf-8"))
    token = m.hexdigest()
    # 写入 token
    redis_client.set(username, token)

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
