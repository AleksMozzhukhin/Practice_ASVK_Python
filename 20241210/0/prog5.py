import asyncio


async def ham(queue, size):
    for i in range(size):
        await asyncio.sleep(1)
        res = await queue.get()
        print(f"\tGot {res}")


async def spam(wait, queue):
    for i in range(6):
        await asyncio.sleep(wait)
        val = f"{wait}:{i}"
        await queue.put(val)
        print(f"Put {val}")


async def main():
    queue = asyncio.Queue()
    await asyncio.gather(ham(queue, 12), spam(0.4, queue), spam(1.6, queue))


asyncio.run(main())
