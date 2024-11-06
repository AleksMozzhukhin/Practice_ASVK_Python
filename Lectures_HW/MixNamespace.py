def mix(*args):
    class Tmp:
        def __str__(self):
            tmp_dict = sorted(self.__dict__.items())
            return ', '.join(f"{i}={j}" for i, j in tmp_dict)

    dictionary = {}
    for i in args:
        for j in dir(i):
            if not j.startswith("_"):
                if not callable(tmp := getattr(i, j)):
                    dictionary[j] = tmp

    tmp = Tmp()
    for i in dictionary:
        setattr(tmp, i, dictionary[i])
    return tmp