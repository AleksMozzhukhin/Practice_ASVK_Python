class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __abs__(self):
        l_1 = ((self.a[1] - self.b[1]) ** 2 + (self.a[0] - self.b[0]) ** 2) ** 0.5
        l_2 = ((self.c[1] - self.b[1]) ** 2 + (self.c[0] - self.b[0]) ** 2) ** 0.5
        l_3 = ((self.a[1] - self.c[1]) ** 2 + (self.a[0] - self.c[0]) ** 2) ** 0.5
        if l_1 and l_2 and l_3 and l_1 + l_2 >= l_3 and l_2 + l_3 >= l_1 and l_3 + l_1 >= l_2:
            p = (l_1 + l_2 + l_3) / 2
            return (p * (p - l_1) * (p - l_2) * (p - l_3)) ** 0.5
        else:
            return 0

    def __bool__(self):
        return abs(self) != 0

    def __lt__(self, other):
        return abs(self) < abs(other)
