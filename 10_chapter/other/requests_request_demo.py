import requests

r =  requests.get("https://httpbin.org/post", json={"key": "value"}, headers={"token": "abc123"})

print(r.request.method)
print(r.request.headers)
print(r.request.url)
print(r.request.body)

