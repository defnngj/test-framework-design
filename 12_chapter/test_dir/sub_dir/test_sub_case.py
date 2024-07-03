# test_dir/sub_dir/test_sub_case.py
import unittest


class TestSubDirCase(unittest.TestCase):
    """子目录测试类"""

    def test_sub_case(self):
        """test sub dir case"""
        self.assertEqual(4 + 4, 8)


if __name__ == '__main__':
    unittest.main()
