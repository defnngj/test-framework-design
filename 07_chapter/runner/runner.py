# runner/runner.py
import functools
import unittest


class MyTestRunner(unittest.TextTestRunner):
    """
    继承&重写 TextTestRunner 类
    """

    def __init__(self, *args, **kwargs):
        """
        增加属性：
        * 黑名单 blacklist 
        * 白名单 whitelist
        """
        self.whitelist = set(kwargs.pop('whitelist', []))
        self.blacklist = set(kwargs.pop('blacklist', []))

        super(MyTestRunner, self).__init__(*args, **kwargs)

    @classmethod
    def test_iter(cls, suite):
        """
        遍历测试套件，生成单个测试
        """
        for test in suite:
            if isinstance(test, unittest.TestSuite):
                for t in cls.test_iter(test):
                    yield t
            else:
                yield test

    def run(self, testlist):
        """
        运行给定的测试用例或测试套件。
        """
        suite = unittest.TestSuite()

        # 在测试列表中添加每个测试，必要时使用跳过机制
        for test in self.test_iter(testlist):
            # 获取用例是否添加了标签，以及标签是否在 白名单 或 黑名单中
            skip = bool(self.whitelist)
            test_method = getattr(test, test._testMethodName)
            test_labels = getattr(test, '_labels', set()) | getattr(test_method, '_labels', set())
            if test_labels & self.whitelist:
                skip = False
            if test_labels & self.blacklist:
                skip = True

            if skip:
                # 针对跳过的用例，通过 skip 替换原始方法
                @functools.wraps(test_method)
                def skip_wrapper(*args, **kwargs):
                    raise unittest.SkipTest('label exclusion')

                skip_wrapper.__unittest_skip__ = True
                if len(self.whitelist) >= 1:
                    skip_wrapper.__unittest_skip_why__ = f'label whitelist {self.whitelist}'
                if len(self.blacklist) >= 1:
                    skip_wrapper.__unittest_skip_why__ = f'label blacklist {self.blacklist}'
                setattr(test, test._testMethodName, skip_wrapper)

            suite.addTest(test)

        super(MyTestRunner, self).run(suite)
