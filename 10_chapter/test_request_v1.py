from common.request_v1 import HttpRequest

http_req = HttpRequest()
http_req.get('http://httpbin.org/get', params={'key': 'value'})
http_req.post('http://httpbin.org/post', data={'key': 'value'})
http_req.put('http://httpbin.org/put', data={'key': 'value'})
http_req.delete('http://httpbin.org/delete')
