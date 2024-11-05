class Rectangle:
    rectcnt = 0

    def __init__(self, x_1, y_1, x_2, y_2):
        self.x_1 = x_1
        self.y_1 = y_1
        self.x_2 = x_2
        self.y_2 = y_2
        self.__class__.rectcnt += 1  # Увеличиваем поле класса во всех классах. Если обратиться без __class__, то мы заведём локальное поле с таким именем
        setattr(self, f"rect_{self.rectcnt}",
                self.rectcnt)  # а здесь __class__ не нужен, так как мы обращаемся к единственной существующей переменной

    def __str__(self):
        return f"({self.x_1},{self.y_1})({self.x_1},{self.y_2})({self.x_2},{self.y_2})({self.x_2},{self.y_1})"

    def __abs__(self):
        return abs(self.x_1 - self.x_2) + abs(self.y_1 - self.y_2)

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __eq__(self, other):
        return abs(self) == abs(other)

    def __mul__(self, other):
        return self.__class__(self.x_1 * other, self.y_1 * other, self.x_2 * other, self.y_2 * other)

    def __rmul__(self, other):
        return self.__class__(self.x_1 * other, self.y_1 * other, self.x_2 * other, self.y_2 * other)

    def __getitem__(self, item):
        return ((self.x_1, self.y_1), (self.x_1, self.x_2), (self.x_2, self.y_1), (self.x_2, self.y_2))[item]

a = Rectangle(5, 5, 6, 6)
print(list(a))