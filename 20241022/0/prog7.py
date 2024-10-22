from curses.ascii import islower
from itertools import *

def gen():
    sum = 0
    for i in count(1):
        sum += 1 / (i * i)
        yield sum

print(list(islice(dropwhile(lambda x: x<=1.6, gen()), 10)))