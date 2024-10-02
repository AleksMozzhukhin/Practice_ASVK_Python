def BinPow(a, n, f):
    if n == 1:
        return a
    elif (n % 2) == 1:
        return f(a, BinPow(a, n - 1, f))
    else:
        b = BinPow(a, n // 2, f)
        return f(b, b)
