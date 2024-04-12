# aiohttp_ws_client_demo.py
import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect('ws://127.0.0.1:8080/echo') as ws:
            # 发送tom
            await ws.send_str("tom")
            async for msg in ws:
                print(f"ws client response, data: {msg.data}")
                break

            # 发送jerry
            await asyncio.sleep(1)
            await ws.send_str("jerry")
            async for msg in ws:
                print(f"ws server response, data: {msg.data}")
                break

            # 发送 close
            await asyncio.sleep(1)
            await ws.send_str("close")


asyncio.run(main())
