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

    def __bool__(self):
        return abs(self) != 0

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __sgn__(self, x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0

    def __contains__(self, item):

        if not bool(item):
            return True
        if self.a == item.a and self.b == item.b and self.c == item.c:
            return True
        for i in (item.a, item.b, item.c):
            side1 = self.__sgn__(
                (self.b[0] - self.a[0]) * (i[1] - self.a[1]) - (self.b[1] - self.a[1]) * (i[0] - self.a[0]))
            side2 = self.__sgn__(
                (self.c[0] - self.b[0]) * (i[1] - self.b[1]) - (self.c[1] - self.b[1]) * (i[0] - self.b[0]))
            side3 = self.__sgn__(
                (self.a[0] - self.c[0]) * (i[1] - self.c[1]) - (self.a[1] - self.c[1]) * (i[0] - self.c[0]))
            if not (side1 == side2 == side3):
                return False
        else:
            return True

    def do_segments_intersect(self, p1, p2, q1, q2):
        """Проверяет, пересекаются ли отрезки (p1, p2) и (q1, q2)."""

        def orientation(p, q, r):
            # Вычисляет ориентированное площадьное произведение для определения ориентации
            return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

        o1 = orientation(p1, p2, q1)
        o2 = orientation(p1, p2, q2)
        o3 = orientation(q1, q2, p1)
        o4 = orientation(q1, q2, p2)

        # Общий случай
        if o1 * o2 < 0 and o3 * o4 < 0:
            return True

        return False

    def __and__(self, other):
        if not bool(self):
            return False
        if any(i == j for i in (self.a, self.b, self.c) for j in (other.a, other.b, other.c)):
            return True
        for p1, p2 in [(self.a, self.b), (self.b, self.c), (self.c, self.a)]:
            for q1, q2 in [(other.a, other.b), (other.b, other.c), (other.c, other.a)]:
                if self.do_segments_intersect(p1, p2, q1, q2):
                    return True
        return False


eval(input())
