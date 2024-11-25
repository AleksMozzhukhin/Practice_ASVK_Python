class Num:
    def __get__(self, obj, cls):
        if hasattr(obj, 'value'):
            return obj.value
        else:
            return 0

    def __set__(self, obj, val):
        if hasattr(val, 'real'):
            obj.value = val
        elif hasattr(val, '__len__'):
            obj.value = len(val)
        else:
            obj.value = 0

    def __delete__(self, obj):
        obj._value = None

t=""
while s:=input():
    t=t+s+"\n"
exec(t)

