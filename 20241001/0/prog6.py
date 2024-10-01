def rbin(previous, n, next):
    previous += [next]
    if n == 1:
        print(*previous, sep="")
    else:
        rbin(previous.copy(), n - 1, 1)
        rbin(previous.copy(), n - 1, 0)


rbin([], 5, 1)
