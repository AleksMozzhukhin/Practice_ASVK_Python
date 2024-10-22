def walk2d():
    x, y = 0, 0
    while True:
        dx, dy = yield x, y
        x += dx
        y += dy


w = walk2d()
print(next(w))
for dx, dy in zip(range(1, 10), range(-10, -20, -1)):
    print(dx, dy, w.send((dx, dy)))
