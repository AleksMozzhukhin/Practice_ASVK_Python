a, b, c = eval(input())
if a > 0 and b > 0 and c > 0 and a < (b + c) and b < (c + a) and c < (a + b):
    print("This is triangle")
else:
    print("This isn't triangle")
# немного читерства
print((max(a, b, c) < sum((a, b, c)) + max(a, b, c)) and (min(a, b, c) > 0))
