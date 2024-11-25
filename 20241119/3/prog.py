class Vowel:
    __slots__ = ("a", "o", "u", 'i', "e", "y", "full")
    answer = 42

    def __init__(self, **kwargs):
        for i in "aouiey":
            try:
                super().__setattr__(i, kwargs[i])
            except KeyError:
                super().__setattr__(i, None)

    def __getattribute__(self, name):
        if name == "full":
            return all(super(Vowel, self).__getattribute__(n) is not None for n in "aouiey")
        else:
            tmp = super(Vowel, self).__getattribute__(name)
            if tmp is None:
                raise AttributeError
            else:
                return tmp

    def __setattr__(self, name, value):
        if name != "full":
            super().__setattr__(name, value)

    def __str__(self):
        ans = ""
        for i in "aouiey":
            try:
                tmp = getattr(self, i)
                ans += f"{i}: {tmp} "
            except AttributeError:
                pass
        return ans.rstrip()


t = ""
while s := input():
    t = t + s + "\n"
exec(t)


