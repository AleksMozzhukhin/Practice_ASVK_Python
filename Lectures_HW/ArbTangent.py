import decimal
import math
from decimal import Decimal


def calculate_pi(n):
    pi = Decimal(13591409)
    ak = Decimal(1)
    for k in range(1, n):
        ak *= -Decimal((6 * k - 5) * (2 * k - 1) * (6 * k - 1)) / Decimal(k * k * k * 26680 * 640320 * 640320)
        val = ak * (13591409 + 545140134 * k)
        pi += val
    pi = pi * Decimal(10005).sqrt() / 4270934400
    return pi ** (-1)


def sin_taylor_series(x, precision):
    sine = decimal.Decimal(x)
    x_squared = decimal.Decimal(x * x)
    term = decimal.Decimal(x)
    sign = decimal.Decimal(-1)
    for n in range(3, precision * 2, 2):
        term *= decimal.Decimal(x_squared / Decimal((n - 1) * n))
        sine += decimal.Decimal(sign * term)
        sign = -sign
    return sine


def cos_taylor_series(x, precision):
    cosine = decimal.Decimal(1)
    x_squared = decimal.Decimal(x * x)
    term = decimal.Decimal(1)
    sign = decimal.Decimal(-1)
    for n in range(2, precision * 2, 2):
        term *= decimal.Decimal(x_squared / Decimal((n - 1) * n))
        cosine += decimal.Decimal(sign * term)
        sign = -sign
    return cosine


def tan_taylor_series(x, precision, acc):
    sinus=decimal.Decimal(sin_taylor_series(x, precision))
    cosinus=decimal.Decimal(cos_taylor_series(x, precision))
    decimal.getcontext().prec=acc
    return decimal.Decimal(sinus / cosinus)


angle = input()
accurate = int(input())
decimal.getcontext().prec = 2000
angle = decimal.Decimal(angle)
pi = calculate_pi(2000)
radians = decimal.Decimal(decimal.Decimal(pi * angle) / 200)
print(tan_taylor_series(radians, 2000, accurate))
