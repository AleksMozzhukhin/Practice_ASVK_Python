import itertools


def slide(seq, n):
    a, b = itertools.tee(seq, 2)
    i = 0
    while True:
        tmp = list(itertools.islice(a, i, i + n))
        if not tmp:
            break
        yield from tmp
        a, b = (itertools.tee(b, 2))
        i += 1


print(*list(eval(input())))
