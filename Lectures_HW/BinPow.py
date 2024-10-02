def BinPow(a, n, f):
    if n == 1:
        return a
    elif (n % 2) == 1:
        return f(a, BinPow(a, n-1, f))
    else:
        b=BinPow(a, n//2, f)
        return f(b,b)

from time import time
start = time()
print(BinPow(3, 5, pow), time()-start)
print(BinPow(2, 33, lambda a, b: a * b), 2**33)
print(BinPow("Se", 7, str.__add__))