import unittest
from aom.shop_object import AuthAPIObject, UserAPIObject, ProductAPIObject

class ShopTest(unittest.TestCase):

    def setUp(self) -> None:
        auth_api = AuthAPIObject("api_key_123")
        self.token = auth_api.get_token("user123")

    def test_user_info(self):
        """
        用户信息查询接口
        """
        user_api = UserAPIObject(self.token)
        user_data = user_api.get_user_data("tom123")
        self.assertEqual(user_data["name"], "tom")

    def test_product_info(self):
        """
        商品信息查询接口
        """
        product_api = ProductAPIObject(self.token)
        product_data = product_api.get_product_data("product123")
        self.assertEqual(product_data["name"], u"潮流T恤")


if __name__ == '__main__':
    unittest.main()
