# extends/depend_extend.py
import functools
from unittest import skipIf


def depend(case=None):
    """
    Use case dependency
    :param case
    :return:
    """

    def wrapper_func(test_func):

        @functools.wraps(test_func)
        def inner_func(self, *args):
            if case == test_func.__name__:
                raise ValueError(f"{case} cannot depend on itself")
            failures = str([fail_[0] for fail_ in self._outcome.result.failures])
            errors = str([error_[0] for error_ in self._outcome.result.errors])
            skipped = str([skip_[0] for skip_ in self._outcome.result.skipped])
            flag = (case in failures) or (case in errors) or (case in skipped)
            test = skipIf(flag, f'{case} failed  or  error or skipped')(test_func)
            try:
                return test(self)
            except TypeError:
                return None

        return inner_func

    return wrapper_func


def if_depend(value):
    """
    Custom skip condition
    :param value
    :return:
    """

    def wrapper_func(function):
        def inner_func(self, *args, **kwargs):
            if not getattr(self, value):
                self.skipTest('Dependent use case not passed')
                pass
            else:
                function(self, *args, **kwargs)

        return inner_func

    return wrapper_func
