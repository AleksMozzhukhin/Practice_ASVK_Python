class Triangle:
    def __init__(self, a, b, c):
        self.a = list(a)
        self.b = list(b)
        self.c = list(c)

    def __abs__(self):
        l_1 = ((self.a[1] - self.b[1]) ** 2 + (self.a[0] - self.b[0]) ** 2) ** 0.5
        l_2 = ((self.c[1] - self.b[1]) ** 2 + (self.c[0] - self.b[0]) ** 2) ** 0.5
        l_3 = ((self.a[1] - self.c[1]) ** 2 + (self.a[0] - self.c[0]) ** 2) ** 0.5
        if l_1 and l_2 and l_3 and l_1 + l_2 >= l_3 and l_2 + l_3 >= l_1 and l_3 + l_1 >= l_2:
            p = (l_1 + l_2 + l_3) / 2
            return (p * (p - l_1) * (p - l_2) * (p - l_3)) ** 0.5
        else:
            return 0

class InvalidInput(Exception):
    def __init__(self, message=""):
        super().__init__(message)


class BadTriangle(Exception):
    def __init__(self, message=""):
        super().__init__(message)


def triangleSquare(inStr):
    try:
        a, b, c = eval(inStr)
        triangle = Triangle(a, b, c)
        tmp = abs(triangle)
    except Exception:
        raise InvalidInput


    if tmp == 0:
        raise BadTriangle
    else:
        return tmp

while True:
    try:
        coord = input()
        square = triangleSquare(coord)
    except BadTriangle:
        print("Not a triangle")
        continue
    except InvalidInput:
        print("Invalid input")
        continue
    else:
        print(f"{square:.2f}")
        break
