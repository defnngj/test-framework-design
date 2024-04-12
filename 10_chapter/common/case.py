import unittest

from jsonschema import validate
from jsonschema.exceptions import ValidationError
from loguru import logger

from .config import ResponseResult

# 定义unittest主方法
main = unittest.main


class TestCase(unittest.TestCase, HttpRequest):
    """
    定义TestCase类，继承 unittest.TestCase 和 HttpRequest
    """

    # def assertPath(self, path: str, value: any) -> None:
    #     """
    #     断言 path 数据
    #     doc: https://jmespath.org/
    #     :param path: JMESpath 提取语法
    #     :param value: 断言值
    #     """
    #     logger.info(f"assertPath -> {path} >> {value}.")
    #     search_value = jmespath.search(path, ResponseResult.response)
    #     self.assertEqual(search_value, value)

    # def assertJSON(self, assert_data, response=None) -> None:
    #     """
    #     断言 JSON 数据
    #     :param assert_data: 断言的JSON数据
    #     :param response: 断言的response，默认为None
    #     """
    #     logger.info(f"assertJSON -> {assert_data}.")
    #     if response is None:
    #         response = ResponseResult.response
    #
    #     AssertInfo.warning = []
    #     AssertInfo.error = []
    #     diff_json(response, assert_data)
    #     if len(AssertInfo.warning) != 0:
    #         logger.warning(AssertInfo.warning)
    #     if len(AssertInfo.error) != 0:
    #         self.assertEqual("Response data", "Assert data", msg=AssertInfo.error)

    def assertSchema(self, schema, response=None) -> None:
        """
        Assert JSON Schema
        doc: https://json-schema.org/
        :param schema: 断言的 schema 数据
        :param response: 断言的response，默认为None
        """
        logger.info(f"assertSchema -> {schema}.")

        if response is None:
            response = ResponseResult.response

        try:
            validate(instance=response, schema=schema)
        except ValidationError as msg:
            self.assertEqual("Response data", "Schema data", msg)
