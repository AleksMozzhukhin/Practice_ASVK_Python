class A:
    pass
class B:
    pass
class C(A,B):
    pass
class D(B, A):
    pass

# class E(C, B, A):
#     pass
# class E(B, A, C):
#     pass
class E(C,D):
    pass