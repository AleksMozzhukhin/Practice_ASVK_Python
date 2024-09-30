a = []
while t := input():
    a.append([*eval(t)])
for i in range(len(a)):
    for j in range(len(a) // 2 + 1):
        a[i][j], a[j][i] = a[j][i], a[i][j]
print(*a, sep='\n')
