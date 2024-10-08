from decimal import Decimal, getcontext
from unicodedata import decimal


def esum(N, one):
    ans = 0
    fact = one
    for i in range(N):
        ans += (one / fact)
        fact *= (i + 1)
    print(ans)


getcontext().prec = 1000
esum(1000, Decimal(1))
esum(100, 1)