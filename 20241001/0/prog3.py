def minus_one(num):
    return minus_one(num - 1) if num > 0 else 0


print(minus_one(5))
