import asyncio
import time


async def late(sec):
    s = time.strftime("%X")
    await asyncio.sleep(sec)
    return sec, s, time.strftime("%X")


async def main():
    print(*await asyncio.gather(late(2), late(3)))


asyncio.run(main())
