class C:
    pass


def fun(a, b):
    print(a, b)


C.a = 123
print(C.a)
e = C()
print(e.a)
C.qwe = 100500
print(e.qwe)
C.fun(1, 2)
print(e.fun(123))
