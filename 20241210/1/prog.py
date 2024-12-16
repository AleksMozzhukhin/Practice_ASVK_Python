import asyncio

async def writer(queue, delay, event):
    counter = 0
    while not event.is_set():
        await asyncio.sleep(delay)
        if event.is_set():
            break
        item = f"{counter}_{delay}"
        await queue.put(item)
        counter += 1

async def stacker(queue, stack, event):
    while True:
        if event.is_set() and queue.empty():
            break
        try:
            item = await asyncio.wait_for(queue.get(), timeout=0.1)
            stack.append(item)
        except asyncio.TimeoutError:
            continue

async def reader(stack, count, delay, event):
    for _ in range(count):
        await asyncio.sleep(delay)
        while True:
            if stack:
                item = stack.pop()
                print(item)
                break
            else:
                await asyncio.sleep(0.01)
    event.set()

async def main(delay1, delay2, delay3, count):
    queue = asyncio.Queue()
    stack = []
    event = asyncio.Event()

    tasks = [
        asyncio.create_task(writer(queue, delay1, event)),
        asyncio.create_task(writer(queue, delay2, event)),
        asyncio.create_task(stacker(queue, stack, event)),
        asyncio.create_task(reader(stack, count, delay3, event)),
    ]

    await tasks[-1]  # Ждем завершения reader

    # Отмена остальных задач
    for task in tasks:
        if not task.done():
            task.cancel()
    await asyncio.gather(*tasks, return_exceptions=True)


input_str = input().strip()
delay1, delay2, delay3, count = map(int, input_str.split(','))
asyncio.run(main(delay1, delay2, delay3, count))