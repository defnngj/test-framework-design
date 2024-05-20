# test_dir/test_sample.py
import unittest


class TestSample(unittest.TestCase):
    """简单的测试类"""

    def test_case_01(self):
        """test case 01"""
        self.assertEqual(1+1, 2)

    def test_case_02(self):
        """test case 02"""
        self.assertEqual(2+2, 4)


if __name__ == '__main__':
    unittest.main()
