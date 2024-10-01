from math import *


def minf(*args):
    def fun(x):
        return min(i(x) for i in args)

    return fun


f = minf(sin, sqrt)
print(f(4))
