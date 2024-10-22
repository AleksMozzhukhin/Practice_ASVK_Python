def gen(x):
    sum = 0
    for i in range(1, x):
        sum += 1 / (i * i)
        yield sum


for i in zip(gen(50), range(50)):
    print(*i)
