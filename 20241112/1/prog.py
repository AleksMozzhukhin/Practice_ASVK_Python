from collections import UserString

class DivStr(UserString):
    def __init__(self, s=""):
        super().__init__(s)

    def __floordiv__(self, other):
        tmp=len(self.data)//other
        return [self.__class__(self.data[i * tmp:(i + 1) * tmp]) for i in range(0, other)]

    def __mod__(self, other):
        tmp = len(self.data) % other
        return self.__class__(self.data[-tmp:] if tmp != 0 else "")


while s:=input():
    exec(s)

