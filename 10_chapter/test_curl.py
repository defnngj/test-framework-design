import requests

from tools.curl import to_curl


def test_to_curl():
    """
    测试转curl命令
    """
    r = requests.get('http://httpbin.org/get', params={'key': 'value'})
    curl_command = to_curl(r.request)
    print(curl_command)

    r = requests.post('http://httpbin.org/post', data={'key': 'value'})
    curl_command = to_curl(r.request)
    print(curl_command)

    # or
    r = requests.delete('http://httpbin.org/delete', json={'key': 'value'})
    curl_command = to_curl(r.request)
    print(curl_command)

    r = requests.put('http://httpbin.org/put', json={'key': 'value'}, headers={"token": "123"})
    curl_command = to_curl(r.request)
    print(curl_command)


if __name__ == '__main__':
    test_to_curl()
