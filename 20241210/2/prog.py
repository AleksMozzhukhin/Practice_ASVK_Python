import asyncio
import random
import math
from copy import copy


async def merge(first_part, second_part, start, middle, finish, event_in1, event_in2, event_out):
    await event_in1.wait()
    await event_in2.wait()

    i, j = start, middle
    k = start

    while i < middle and j < finish:
        if first_part[i] <= first_part[j]:
            second_part[k] = first_part[i]
            i += 1
        else:
            second_part[k] = first_part[j]
            j += 1
        k += 1

    while i < middle:
        second_part[k] = first_part[i]
        i += 1
        k += 1

    while j < finish:
        second_part[k] = first_part[j]
        j += 1
        k += 1

    event_out.set()


async def copy_segment(previous, target, start, finish, event_in, event_out):
    await event_in.wait()
    for k in range(start, finish):
        target[k] = previous[k]

    event_out.set()


async def mtasks(data):
    n = len(data)
    if n == 0:
        return [], data

    tasks = []
    levels = math.ceil(math.log2(n)) if n > 1 else 1
    events = [[asyncio.Event() for _ in range(n)]]
    for event in events[0]:
        event.set()

    source = copy(data)
    destination = [0] * n

    for level in range(levels):
        size = 2 ** level
        next_size = size * 2
        num_merges = math.ceil(n / next_size)
        events.append([asyncio.Event() for _ in range(num_merges)])

        for i in range(num_merges):
            start = i * next_size
            middle = min(start + size, n)
            finish = min(start + next_size, n)

            event_in1 = events[level][i * 2] if (i * 2) < len(events[level]) else None
            event_in2 = events[level][i * 2 + 1] if (i * 2 + 1) < len(events[level]) else None

            event_out = events[level + 1][i]

            if event_in1 and event_in2:
                task = asyncio.create_task(
                    merge(source, destination, start, middle, finish, event_in1, event_in2, event_out))
                tasks.append(task)
            elif event_in1:
                task = asyncio.create_task(
                    copy_segment(source, destination, start, finish, event_in1, event_out))
                tasks.append(task)

        source, destination = destination, source

    final_sorted = source
    return tasks, final_sorted


async def main(A):
    tasks, final_sorted = await mtasks(A)
    print(len(tasks))
    random.shuffle(tasks)
    await asyncio.gather(*tasks)
    return final_sorted


# t=""
# while s:=input():
#     t=t+s+"\n"
# exec(t)
random.seed(1337)
A = random.choices(range(10), k=33)
B = asyncio.run(main(A))
print(*A)
print(*B)
print(B == sorted(A))
