class Rectangle:
    rectcnt = 0

    def __init__(self, x_1, y_1, x_2, y_2):
        self.x_1 = x_1
        self.y_1 = y_1
        self.x_2 = x_2
        self.y_2 = y_2
        self.__class__.rectcnt += 1

    def __str__(self):
        return f"({self.x_1},{self.y_1})({self.x_1},{self.y_2})({self.x_2},{self.y_2})({self.x_2},{self.y_1})"


a = Rectangle(5, 5, 6, 6)
print(a.rectcnt)
b= Rectangle(5, 5, 6, 6)
print(b.rectcnt)

