class C:
    def __init__(self):
        self._age = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > 128:
            print("to old")
            raise ValueError
        self._age = value

    @age.getter
    def age(self):
        if self._age == 42:
            print("secret value")
            return -1
        return self._age

    @age.deleter
    def age(self):
        del self._age

c=C()
c.age = 42
print(c.age)
