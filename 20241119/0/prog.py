def isint(f):
    def newfun(*args):
        for i in args:
            if type(i) != int:
                raise TypeError
        res = f(*args)
        return res
    return newfun

@isint
def fun(a,b):
    return a*2+b

print(fun(2,3.6))