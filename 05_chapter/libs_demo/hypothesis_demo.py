# hypothesis_demo.py
import unittest
from hypothesis import given, settings
import hypothesis.strategies as st


def add(a: int, b: int):
    """被测试函数"""
    return a + b


class AddTest(unittest.TestCase):

    @settings(max_examples=10)
    @given(a=st.integers(), b=st.integers())
    def test_case(self, a, b):
        print(f"测试数据：a-> {a}, b-> {b}")
        c2 = add(a, b)
        self.assertIsInstance(c2, int)


if __name__ == '__main__':
    unittest.main()
