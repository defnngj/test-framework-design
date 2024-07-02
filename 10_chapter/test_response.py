import requests

from tools.response import check_response


@check_response(
    describe="获取用户登录token",
    status_code=200,
    ret="form.token",
    check={"headers.Host": "httpbin.org"},
    debug=True)
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
        "token": "token123"
    }
    r = requests.post(url, data=data)
    return r


if __name__ == '__main__':
    token = get_token("jack", "pawd123")
    print(f"get token: {token}")
