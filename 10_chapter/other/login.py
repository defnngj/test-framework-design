import json
import requests


def get_token(username, password):
    """
    获取用户登录token
    :param username:
    :param password:
    """

    url = "http://httpbin.org/post"

    data = {
        "username": username,
        "password": password,
        "token": "token123"  # 假装这是接口返回的toKen
    }
    r = requests.post(url, data=data)

    if r.status_code != 200:
        raise ValueError("接口请求失败")

    try:
        r.json()
    except json.decoder.JSONDecodeError:
        raise ValueError("接口不是JSON格式")

    if r.json()["headers"]["Host"] != "httpbin.org":
        raise ValueError("接口返回必要参数错误")

    try:
        user_token = r.json()["form"]["token"]
    except KeyError:
        user_token = ""

    return user_token


if __name__ == '__main__':
    token = get_token("admin", "abc123")
    print(f"get token: {token}")
