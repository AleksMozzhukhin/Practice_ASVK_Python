class ExceptionTree:
    def __init__(self):
        self.ex = {1: type("Exception-1", (Exception,), {"n": 1})}

    def __call__(self, e):
        if e not in self.ex:
            self.ex[e] = type(f"Exception-{e}", (self(e // 2),), {"n": e})
        return self.ex[e]
