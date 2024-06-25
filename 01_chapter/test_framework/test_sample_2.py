"""
test_sample_2.py
QTAF例子
"""
from testbase.testcase import TestCase


class HelloTest(TestCase):
    """
    第一条用例
    """
    owner = "foo"
    status = TestCase.EnumStatus.Ready
    priority = TestCase.EnumPriority.Normal
    timeout = 1

    def run_test(self):
        """
        测试步骤
        """
        self.start_step("第一个测试步骤")
        self.log_info("hello")
        self.assert_("检查计算结果", 2 + 2 == 4)


if __name__ == '__main__':
    HelloTest().debug_run()
