def istype(typ):
    def decorator(fun):
        def newfun(*args):
            for i in args:
                if not isinstance(i, typ):
                    raise ValueError
            return [fun(*args) for i in range(3)]
        return newfun
    return decorator

@istype(float)
def simplefun(N):
    return N*2+1

print(*simplefun(4))