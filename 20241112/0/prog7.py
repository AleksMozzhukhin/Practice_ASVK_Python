def small_div(x, y, eps):
    if y<eps:
        raise ZeroDivisionError("Look's like divisor is like a zero")
    else:
        return x/y

try:
    print(small_div(2,3,0.1))
    print(small_div(2,0.01,0.1))
except ZeroDivisionError:
    print("Be careful about division((((")