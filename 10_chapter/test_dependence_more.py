import unittest

from tools.dependence import redis_client, dependent_func


class DependentTest(unittest.TestCase):

    def get_name(self):
        return "tom"

    def get_age(self):
        return 23

    @dependent_func(get_name, key_name="name")
    @dependent_func(get_age, key_name="age")
    def test_case(self):
        """
        sample test case
        """
        name = redis_client.get("name")
        age = redis_client.get("age")


if __name__ == '__main__':
    unittest.main()
