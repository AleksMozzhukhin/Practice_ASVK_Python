from math import *

w = 65
h = 140
a, b = eval(input()) #границы интервала, в котором выводим график
for i in range(h):
    x = (b - a) / (h - 1) * i + a
    y = sin(x)
    shift = round((y + 1) / 2 * w)
    print(" " * shift, "*")
