def fun(a, b):
    return lambda x: a * x + b


f = fun(2, 1)
print(f(2))
