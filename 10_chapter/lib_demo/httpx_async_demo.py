# httpx_async_demo.py
import asyncio
import httpx

async def main():
    async with httpx.AsyncClient() as client:
        r = await client.get('https://www.example.com/')
        print(f"状态码： {r.status_code}")
        print(f"返回数据： {r.text}")

asyncio.run(main())
