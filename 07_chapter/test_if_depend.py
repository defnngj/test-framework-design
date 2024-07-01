import unittest

from extends.depend_extend import if_depend


class TestIfDepend(unittest.TestCase):
    depend_flag = True

    def test_001(self):
        TestIfDepend.depend_flag = False  # 修改 depend_flag 为 False

    @if_depend("depend_flag")
    def test_002(self):
        ...


if __name__ == '__main__':
    unittest.main()
