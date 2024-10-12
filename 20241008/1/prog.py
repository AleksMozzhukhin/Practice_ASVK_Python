from decimal import Decimal

values = list(input().split(','))
dec_values = []
s = int(values[0])
st_first = int(values[2])
mn_first = values[3 + st_first:2:-1]
a = Decimal(0)
for i in range(st_first, -1, -1):
    a += Decimal(Decimal(eval(mn_first[i])) * (s ** i))
st_second = int(values[st_first + 3 + 1])
mn_second = values[-1:st_first + 3 + 1:-1]
b = Decimal(0)
for i in range(st_second, -1, -1):
    b += Decimal(Decimal(eval(mn_second[i])) * (s ** i))
print((a / b) == Decimal(eval(values[1])))
