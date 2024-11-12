class A:
    def __str__(self):
        return "A"

class B(A):
    def __str__(self):
        return f"B:{super().__str__()}"

class C(B):
    def __str__(self):
        return f"C:{super().__str__()}"

print(C())