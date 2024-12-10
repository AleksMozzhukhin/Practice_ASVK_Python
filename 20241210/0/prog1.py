import asyncio


async def squarer(a):
    return a * a


async def doubler(a):
    return 2 * a


async def main(x, y):
    dx, dy = await asyncio.gather(squarer(x), squarer(y))
    dx, dy = await asyncio.gather(doubler(dx), doubler(dy))
    return dx, dy


print(asyncio.run(main(5, 4)))
