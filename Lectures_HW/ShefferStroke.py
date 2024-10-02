def sheff(a, b):
    if a and b:
        return False
    elif not (a or b):
        return True
    else:
        return a if a else b