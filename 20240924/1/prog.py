first, last = eval(input())
print(list(i for i in range(first, last) if all(i % n != 0 for n in range(2, int(i ** 0.5) + 1))))
