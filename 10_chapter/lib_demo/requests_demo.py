# requests_demo.py
import requests

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print(f"返回状态码： {r.status_code}")
print(f"返回数据： {r.json()}")