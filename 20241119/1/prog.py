def objcount(cls):
    cls.counter = 0
    ___init___ = getattr(cls, '__init__', None)
    ___del___ = getattr(cls, '__del__', None)


    def new_init(self, *args, **kwargs):
        cls.counter += 1
        if ___init___:
            ___init___(self, *args, **kwargs)

    def new_del(self):
        cls.counter -= 1
        if ___del___:
            ___del___(self)

    cls.__init__ = new_init
    cls.__del__ = new_del
    return cls


t = ""
while s := input():
    t = t + s + "\n"

exec(t)
