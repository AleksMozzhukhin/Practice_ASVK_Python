import sys
from string import ascii_letters
from pympler.asizeof import asizeof


class Slotter:
    __slots__ = tuple(ascii_letters)

    def __init__(self):
        for attr in ascii_letters:
            setattr(self, attr, attr)


class Trad:
    def __init__(self):
        for attr in ascii_letters:
            setattr(self, attr, attr)


s = [Slotter() for i in range(1000)]
t = [Trad() for i in range(1000)]
# print(sys.getsizeof(Slotter), sys.getsizeof(Trad))
# print(sys.getsizeof(s), sys.getsizeof(t))
# print(asizeof(, asizeof())
print(asizeof(s), asizeof(t))
