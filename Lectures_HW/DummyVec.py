class vector:
    def __init__(self, *coordinates):
        self.coordinates = list(*coordinates)

    def __add__(self, other):
        return self.__class__(self.coordinates[i] + other[i] for i in range(len(self.coordinates)))

    def __radd__(self, other):
        return self.__class__(self.coordinates[i] + other[i] for i in range(len(self.coordinates)))

    def __str__(self):
        return ":".join(str(i) for i in self.coordinates)

    def __getitem__(self, key):
        return self.coordinates[key]

    def __matmul__(self, other):
        return sum(self.coordinates[i] * other[i] for i in range(len(self.coordinates)))
