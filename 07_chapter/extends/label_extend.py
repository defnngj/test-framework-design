# extends/label_extend.py


def label(*labels):
    """
    测试用例分类标签

    Usage:
        class MyTest(unittest.TestCase):
            
            @label('quick')
            def test_foo(self):
                pass
    """

    def inner(cls):
        """
        类/方法添加标签
        """
        cls._labels = set(labels) | getattr(cls, '_labels', set())
        return cls

    return inner
