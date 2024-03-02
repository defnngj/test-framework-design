# ddt_demo2.py
import unittest
from ddt import ddt, file_data


@ddt
class TestDDT(unittest.TestCase):

    @file_data('test_data/test_data.json')
    def test_file_data_json(self, start, end, value):
        self.assertLess(start, end)
        self.assertLess(value, end)
        self.assertGreater(value, start)

    @file_data('test_data/test_data.yaml')
    def test_file_data_yaml(self, start, end, value):
        self.assertLess(start, end)
        self.assertLess(value, end)
        self.assertGreater(value, start)


if __name__ == '__main__':
    unittest.main(verbosity=2)
