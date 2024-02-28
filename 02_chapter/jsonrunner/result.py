import sys
from unittest import TestResult


class _TestResult(TestResult):
    """
    继承 unittest.TestResult 类，重写通过/失败/错误/跳过等方法
    """

    def __init__(self, verbosity=1):
        TestResult.__init__(self)
        self.success_count = 0
        self.failure_count = 0
        self.error_count = 0
        self.skip_count = 0
        self.verbosity = verbosity
        self.result = []

    def startTest(self, test):
        TestResult.startTest(self, test)

    def addSuccess(self, test):
        self.success_count += 1
        TestResult.addSuccess(self, test)
        self.result.append((0, test, ''))
        if self.verbosity > 1:
            sys.stderr.write('ok')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('.'+str(self.success_count))

    def addFailure(self, test, err):
        self.failure_count += 1
        TestResult.addFailure(self, test, err)
        _, _exc_str = self.failures[-1]
        self.result.append((1, test, _exc_str))
        if self.verbosity > 1:
            sys.stderr.write('F')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('F')

    def addError(self, test, err):
        self.error_count += 1
        TestResult.addError(self, test, err)
        _, _exc_str = self.errors[-1]
        self.result.append((2, test, _exc_str))
        if self.verbosity > 1:
            sys.stderr.write('E')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('E')

    def addSkip(self, test, reason):
        self.skip_count += 1
        TestResult.addSkip(self, test, reason)
        self.result.append((3, test, reason))
        if self.verbosity > 1:
            sys.stderr.write('S')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('S')
