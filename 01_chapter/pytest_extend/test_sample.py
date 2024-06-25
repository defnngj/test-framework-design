"""
pytest扩展方式
"""
import pytest


# 调用钩子函数 name()
def test_hello(name):
    greetings = f"hello {name}"
    print(greetings)
    assert greetings == "hello 虫师"


# 使用装饰器
@pytest.mark.parametrize(
    'a, b',
    [
        (1, 2),
        (2, 3),
        (3, 4),
    ])
def test_add(a, b):
    print(f"a:{a}, b:{b}")
    assert a + 1 == b


# 使用命令行参数 base_url
def test_cmd(base_url):
    print(f"base_url: {base_url}")
    assert "http" in base_url
