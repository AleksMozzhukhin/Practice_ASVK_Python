class IsType:
    def __init__(self, typ):
        self.typ = typ
        # self.typ = typ

    def __call__(self, fun):
        def newfun(*args):
            if any(not isinstance(i, self.typ) for i in args):
                raise TypeError("Type must be of type %s" % self.typ)
            return fun(*args)
        return newfun

@IsType(float)
def simplefun(N):
    return N*2+1

print(simplefun(4))