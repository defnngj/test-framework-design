# ddt_demo.py
import unittest

from ddt import ddt, data, unpack


@ddt
class TestDTT(unittest.TestCase):

    @data([1, 2, 3], [4, 5, 9], [6, 7, 13])
    @unpack
    def test_add_list(self, a, b, c):
        self.assertEqual(a + b, c)

    @data(("Hi", "HI"), ("hello", "HELLO"), ("world", "WORLD"))
    @unpack
    def test_upper_tuple(self, s1, s2):
        self.assertEqual(s1.upper(), s2)

    @data({"d": "hello world", "t": str},
          {"d": 110, "t": int},
          {"d": True, "t": bool})
    @unpack
    def test_data_type_dict(self, d, t):
        self.assertTrue(isinstance(d, t))


if __name__ == '__main__':
    unittest.main(verbosity=2)
