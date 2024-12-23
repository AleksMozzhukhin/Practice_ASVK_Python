def calc(s, t, u):
    def f1(x):
        return eval(s)

    def f2(x):
        return eval(t)

    def f3(x, y):
        return eval(u)

    def final(x):
        return f3(f1(x), f2(x))

    return final


from math import *

a, b, c = eval(input())
num = eval(input())
F=calc(a,b,c)
print(F(num))