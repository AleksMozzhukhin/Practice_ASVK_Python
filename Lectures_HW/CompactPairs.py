from string import ascii_letters


class Pairs:
    __slots__ = tuple(ascii_letters + "_")

    def __init__(self, n):
        self._ = n
        for i in ascii_letters:
            setattr(self, i, n)
            n = n + 1 if n != 52 else 1

    def __str__(self):
        final_string = ""
        tmp = ascii_letters[52 - self._ + 1:]
        for i in tmp:
            final_string += f"{i} "
        tmp = ascii_letters[:52 - self._ + 1]
        for i in tmp:
            final_string += f"{i} "

        return final_string.rstrip()
