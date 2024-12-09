class Square:
    __match_args__ = ('x', 'y', 'w')

    def __init__(self, x, y, w):
        self._x = x
        self._y = y
        self._w = w

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value


    @property
    def w(self):
        return self._w

    @w.setter
    def w(self, value):
        self._w = value

    @property
    def h(self):
        return self._w

    @h.setter
    def h(self, value):
        self.w = value

    @property
    def s(self):
        return self._w * self.h

    @s.setter
    def s(self, value):
        pass

    @property
    def center(self):
        return (self._x + self._w / 2, self._y + self._w / 2)

    @center.setter
    def center(self, value):
        if isinstance(value, tuple):
            if len(value) == 2:
                new_center_x, new_center_y = value
                self._x = new_center_x - self._w / 2
                self._y = new_center_y - self._w / 2
            elif len(value) == 4:
                current_center_x, current_center_y, shift_x, shift_y = value
                new_center_x = current_center_x + shift_x
                new_center_y = current_center_y + shift_y
                self._x = new_center_x - self._w / 2
                self._y = new_center_y - self._w / 2

    def __repr__(self):
        return f"Square(x={self._x}, y={self._y}, w={self._w})"
