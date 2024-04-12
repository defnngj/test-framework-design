
class AssertInfo:
    """暂存断言信息"""
    warning = []
    error = []


def diff_json(response_data, assert_data):
    """
    递归：对比两个 JSON 数据格式
    """

    if isinstance(response_data, dict) and isinstance(assert_data, dict):
        # 字典格式
        for key in assert_data:
            if key not in response_data:
                AssertInfo.error.append(f"错误: Response没有key: {key}")
        for key in response_data:
            if key in assert_data:
                # 递归
                diff_json(response_data[key], assert_data[key])
            else:
                AssertInfo.warning.append(f"警告: 断言数据没有key: {key}")

    elif isinstance(response_data, list) and isinstance(assert_data, list):
        # 列表格式
        if len(response_data) == 0:
            AssertInfo.warning.append("警告: response是[]")
        else:
            if isinstance(response_data[0], dict):
                try:
                    response_data = sorted(
                        response_data,
                        key=lambda x: x[list(response_data[0].keys())[0]])
                except TypeError:
                    response_data = response_data
            else:
                response_data = sorted(response_data)

        if len(response_data) != len(assert_data):
            AssertInfo.warning.append(
                f"警告：列表长度不同: '{len(response_data)}' != '{len(assert_data)}'")

        if len(assert_data) > 0:
            if isinstance(assert_data[0], dict):
                try:
                    assert_data = sorted(
                        assert_data,
                        key=lambda x: x[list(assert_data[0].keys())[0]])
                except TypeError:
                    assert_data = assert_data
            else:
                assert_data = sorted(assert_data)

        for src_list, dst_list in zip(response_data, assert_data):
            # 递归
            diff_json(src_list, dst_list)
    else:
        if str(response_data) != str(assert_data):
            AssertInfo.error.append(f"错误: 数据不相等: {response_data}")


# if __name__ == '__main__':
#     response_data = {
#         "user_list": [
#             {
#                 "id": 1,
#                 "name": "tom",
#                 "hobby": ["basketball", "swimming"]
#             },
#             {
#                 "id": 2,
#                 "name": "jack",
#                 "hobby": ["skiing", "reading", "taking"]
#             }
#         ]
#     }
#     assert_data = {
#         "user_list": [
#             {
#                 "id": 1,
#                 "name": "tom",
#                 "hobby": ["basketball", "swimming"]
#             },
#             {
#                 "id": 2,
#                 "name": "jack",
#                 "hobby": ["skiing", "reading"]
#             }
#         ]
#     }
#     diff_json(response_data, assert_data)
#     print(AssertInfo.data)
