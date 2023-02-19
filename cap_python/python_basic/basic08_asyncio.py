# python内置协程包 asyncio
import asyncio


async def print_info(n):
    while True:
        print(n)
        # 在协程中要使用asyncio.sleep 不能用time.sleep
        # await 会阻塞等待返回
        await asyncio.sleep(1)


async def main():
    for i in range(1000000):
        # 开启协程
        asyncio.create_task(print_info(i))
    await asyncio.sleep(30)


# 启动协程
asyncio.run(main())
