class A:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return f"<{self.val}>"


print(A(9))


class B(A):
    def __init__(self, val):
        super().__init__(val)
        self.val += 1
