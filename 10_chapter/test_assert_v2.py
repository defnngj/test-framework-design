from common import case


class MyHttpTest(case.TestCase):

    def test_assert_path(self):
        """
        测试 assertPath() 断言方法
        """
        params = {
            "user_list": [
                {
                    "id": 1,
                    "name": "tom",
                    "hobby": ["basketball", "swimming"]
                },
                {
                    "id": 2,
                    "name": "jack",
                    "hobby": ["skiing", "reading"]
                }
            ]
        }

        self.assertPath("json.user_list[0].id", 1)
        self.assertPath("json.user_list[0].name", "tom")
        self.assertPath("json.user_list[0].hobby[0]", "basketball")
        self.assertPath("json.user_list[1].name", "jack")
        self.assertPath("json.user_list[1].hobby", ["skiing", "reading"])

    def test_assert_json(self):
        """
        测试 assertJSON() 断言方法
        """
        payload = {"name": "tom", "hobby": ["basketball", "swim"]}
        resp = self.get("http://httpbin.org/get", params=payload)

        # 1.从整个response中断言。
        assert_data1 = {
            "args": {
                "hobby": ["swim", "basketball"],
                "name": "tom"
            }
        }
        self.assertJSON(assert_data1)

        # 2. 从部分 response 中断言。
        assert_data2 = {
            "hobby": ["swim", "basketball"],
            "name": "tom"
        }
        self.assertJSON(assert_data2, resp.json()["args"])

    def test_assert_schema(self):
        """
        测试 assertSchema() 断言方法
        """
        payload = {"hobby": ["basketball", "swim"], "name": "tom"}
        resp = self.get("http://httpbin.org/get", params=payload)

        # 1.从整个response中断言
        assert_data1 = {
            "type": "object",
            "properties": {
                "args": {
                    "type": "object",
                    "properties": {
                        "hobby": {
                            "type": "array", "items": {"type": "string"}
                        },
                        "name": {
                            "type": "string"
                        }
                    }
                }
            }
        }
        self.assertSchema(assert_data1)

        # 2.从部分 response 中断言
        assert_data2 = {
            "type": "object",
            "properties": {
                "hobby": {
                    "type": "array", "items": {"type": "string"}
                },
                "name": {
                    "type": "string"
                }
            }
        }
        self.assertSchema(assert_data2, resp.json()["args"])


if __name__ == '__main__':
    case.main()
