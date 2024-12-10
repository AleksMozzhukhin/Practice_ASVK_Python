import asyncio


async def prod(q):
    for i in range(5):
        st = f"value_{i}"
        await q.put(st)
        print(f"prod: put {st} to q1")
        await asyncio.sleep(1)


async def mid(q1, q2):
    while True:
        res = await q1.get()
        print(f"mid: got {res} from q1")
        await q2.put(res)
        print(f"mid put {res} to q2")


async def cons(q):
    while True:
        res = await q.get()
        print(f"cons: got {res} from q2")
    return


async def main():
    q1 = asyncio.Queue()
    q2 = asyncio.Queue()
    await asyncio.gather(cons(q2), prod(q1), mid(q1, q2))


asyncio.run(main())
