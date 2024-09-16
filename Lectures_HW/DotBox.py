x = []
y = []
z = []
while tmp := input():
    tmp = eval(tmp)
    x.append(tmp[0])
    y.append(tmp[1])
    z.append(tmp[2])
print((max(x) - min(x)) * (max(y) - min(y)) * (max(z) - min(z)))
