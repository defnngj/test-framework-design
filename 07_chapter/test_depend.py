import unittest

from extends.depend_extend import depend


class TestDepend(unittest.TestCase):

    def test_001(self):
        print("test_001")
        self.assertEqual(1 + 1, 3)

    @depend("test_001")
    def test_002(self):
        print("test_002")

    @depend("test_002")
    def test_003(self):
        print("test_003")


if __name__ == '__main__':
    unittest.main()

    # 手动控制用例的添加
    # suite = unittest.TestSuite()
    # suite.addTests([
    #     TestDepend("test_001"),
    #     TestDepend("test_002"),
    #     TestDepend("test_003"),
    # ])
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
