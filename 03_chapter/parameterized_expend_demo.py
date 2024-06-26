# parameterized_expend_demo.py
import unittest

from extend.data_conversion import csv_to_list
from extend.data_conversion import excel_to_list
from extend.data_conversion import file_data
from extend.data_conversion import json_to_list
from extend.data_conversion import yaml_to_list
from extend.parameterized_extend import data


class ParamTest(unittest.TestCase):

    @data([
        ("2 and 3", 2, 3, 5),
        ("10 and 20", 10, 20, 30),
        ("hello and word", "hello", "world", "helloworld"),
    ])
    def test_tuple_add(self, _, a, b, expected):
        self.assertEqual(a + b, expected)

    @data([
        ["2 and 3", 2, 3, 5],
        ["10 and 20", 10, 20, 30],
        ["hello and word", "hello", "world", "helloworld"],
    ])
    def test_list_add(self, _, a, b, expected):
        self.assertEqual(a + b, expected)

    @data([
        {"scene": "username_is_null", "username": "", "password": "123"},
        {"scene": "password_is_null", "username": "user", "password": ""},
        {"scene": "login_success", "username": "user", "password": "123"},
    ])
    def test_dict_data(self, scene, username, password):
        ...


class FileParamTest(unittest.TestCase):

    @data(json_to_list("test_data/json_data.json", key="login"))
    def test_login_json(self, name, username, password):
        print(f"scene: {name}, username: '{username}' password: '{password}'")

    @data(yaml_to_list("test_data/yaml_data.yaml", key="login"))
    def test_login_yaml(self, name, username, password):
        print(f"scene: {name}, username: '{username}' password: '{password}'")

    @data(csv_to_list("test_data/csv_data.csv", line=2))
    def test_login_csv(self, name, username, password):
        print(f"scene: {name}, username: '{username}' password: '{password}'")

    @data(excel_to_list("test_data/excel_data.xlsx", sheet="Sheet1", line=2))
    def test_login_excel(self, name, username, password):
        print(f"scene: {name}, username: '{username}' password: '{password}'")


class FileDataTest(unittest.TestCase):

    @file_data("test_data/json_data.json", key="login")
    def test_login_json(self, name, username, password):
        print(f"case: {name}, username: '{username}' password: '{password}'")

    @file_data("test_data/yaml_data.yaml", key="login")
    def test_login_yaml(self, name, username, password):
        print(f"case: {name}, username: '{username}' password: '{password}'")

    @file_data("test_data/csv_data.csv", line=2)
    def test_login_csv(self, name, username, password):
        print(f"case: {name}, username: '{username}' password: '{password}'")

    @file_data("test_data/excel_data.xlsx", sheet="Sheet1", line=2)
    def test_login_excel(self, name, username, password):
        print(f"case: {name}, username: '{username}' password: '{password}'")


if __name__ == '__main__':
    unittest.main()
