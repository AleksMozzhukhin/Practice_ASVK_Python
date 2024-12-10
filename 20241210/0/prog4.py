import asyncio


async def snd(event):
    event.set()
    print(f"snd generated evsnd")


async def mid(k, event, e):
    await event.wait()
    print(f"mid received evsnd")
    e.set()
    print(f"mid generated evmid{k}")


async def rcv(e0, e1):
    await e0.wait()
    print(f"rcv received evmid0")
    await e1.wait()
    print(f"rcv received evmid1")


async def main():
    evsnd = asyncio.Event()
    evmid0 = asyncio.Event()
    evmid1 = asyncio.Event()
    await asyncio.gather(
        rcv(evmid0, evmid1),
        mid(1, evsnd, evmid1),
        mid(0, evsnd, evmid0),
        snd(evsnd),
    )


asyncio.run(main())
