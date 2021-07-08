import asyncio


async def func():
    print("aaa")

if __name__ == '__main__':
    g = func()
    asyncio.get_event_loop().run_until_complete(g)
