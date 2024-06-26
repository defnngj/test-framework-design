# parameterized_demo.py
import unittest

from parameterized import parameterized


class AddTestCase(unittest.TestCase):

    @parameterized.expand([
        ("2 and 3", 2, 3, 5),
        ("10 and 20", 10, 20, 30),
        ("hello and world", "hello", "world", "helloworld"),
    ])
    def test_add(self, _, a, b, expected):
        self.assertEqual(a + b, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
