from itertools import filterfalse

n = 13
print(*filterfalse(lambda x: (x % n != 0 or x % 2 == 0), range(1, 1000)))
