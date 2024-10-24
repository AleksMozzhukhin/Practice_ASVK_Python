def fib(m, n):
    first = 1
    second = 1
    for i in range(2, m):
        second, first = first, first + second
    for i in range(m, m + n):
        second, first = first, first + second
        yield first


a, b = eval(input())
print(*fib(a, b))
