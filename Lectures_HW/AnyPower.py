from math import log

number = int(input())
for i in range(2, 1001):
    if ((x := log(number, i)) == int(x)) and i != number:
        print("YES")
        break
else:
    print("NO")
