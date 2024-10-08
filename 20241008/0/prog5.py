from math import *


def show(screen):
    print("\n".join("".join(s) for s in screen))


def scale(a, b, A, B, x):
    return (B - A) * (x - a) / (b - a) + A


w = 120
h = 30
a = 0
b = 12
screen = [[" "] * w for i in range(h)]
for i in range(w):
    x = scale(0, w - 1, a, b, i)
    y = sin(x)
    shift = (scale(-1, 1, 0, h - 1, y))
    screen[round(shift)][i] = "*"
show(screen)
