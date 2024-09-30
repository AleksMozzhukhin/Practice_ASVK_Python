a = []
while t := input():
    a.append([*eval(t)])
if all(len(i) == len(a[0]) for i in a) and len(a) == len(a[0]):
    for i in range(len(a)):
        for j in range(len(a) // 2 + 1):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    print(*a, sep='\n')
else:
    print("Matrix isn't square")
    exit()