import unittest
from extends.depend_extend import if_depend


class TestIfDepend(unittest.TestCase):

    depend_tag = True

    def test_001(self):
        TestIfDepend.depend_tag = False  # 修改 depend_tag 为 False

    @if_depend("depend_tag")
    def test_002(self):
        ...


if __name__ == '__main__':
    unittest.main()

