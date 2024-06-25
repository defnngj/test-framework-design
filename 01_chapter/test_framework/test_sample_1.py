"""
test_sample_1.py
unittest例子
"""
import unittest


class MyTest(unittest.TestCase):

    def test_case(self):
        self.assertEqual(2 + 2, 4)


if __name__ == '__main__':
    unittest.main()
