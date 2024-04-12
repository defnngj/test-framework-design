# aiohttp_server_demo.py
import aiohttp
from aiohttp import web


# HTTP服务
async def http_handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


# WebSocket服务
async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                await ws.send_str(f'Hello, {msg.data}')
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print(f'ws connection closed with exception {ws.exception()}')

    print('websocket connection closed')

    return ws


app = web.Application()
app.add_routes([
    web.get('/hello/', http_handle),
    web.get('/hello/{name}', http_handle),
    web.get('/echo', websocket_handler)
])

if __name__ == '__main__':
    web.run_app(app, host="127.0.0.1", port=8080)
