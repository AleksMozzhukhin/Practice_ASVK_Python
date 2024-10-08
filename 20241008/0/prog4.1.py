from math import *


def scale(a, b, A, B, x):
    return (B - A) * (x - a) / (b - a) + A


w = 65
h = 140
a, b = eval(input())  # границы интервала, в котором выводим график
for i in range(h):
    x = scale(0, h - 1, a, b, i)
    y = sin(x)
    shift = (scale(-1, 1, 0, w - 1, y))
    print(" " * round(shift), "*")
