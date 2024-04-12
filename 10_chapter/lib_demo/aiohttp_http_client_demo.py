# aiohttp_http_client_demo.py
import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://127.0.0.1:8080/hello/jack') as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])
            text = await response.text()
            print("Response text:", text)


asyncio.run(main())
