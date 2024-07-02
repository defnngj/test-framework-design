# httpx_sync_demo.py
import httpx

r = httpx.get('https://www.example.org/')
print(f"状态码： {r.status_code}")
print(f"返回数据： {r.text}")
