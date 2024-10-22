def f(x):
    yield ">"
    yield from x
    yield "<"
    return len(x)

g=f("qwe")
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# print(list(f("qwe")))
