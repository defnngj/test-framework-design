import unittest
from extends.label_extend import label
from runner.runner import MyTestRunner


class MyTest(unittest.TestCase):

    @label("base")
    def test_label_base(self):
        self.assertEqual(1+1, 2)

    @label("slow")
    def test_label_slow(self):
        self.assertEqual(1, 2)

    def test_no_label(self):
        self.assertEqual(2+3, 5)


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTests([
        MyTest("test_label_base"),
        MyTest("test_label_slow"),
        MyTest("test_no_label")
    ])
    # runner = MyTestRunner(whitelist=["base"], verbosity=2)  # 白名单
    runner = MyTestRunner(blacklist=["slow"], verbosity=2)    # 黑名单
    runner.run(suit)
