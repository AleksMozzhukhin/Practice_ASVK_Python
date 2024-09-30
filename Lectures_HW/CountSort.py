mas = [[0 for j in range(101)] for i in range(101)]

while tmp := input():
    a = eval(tmp)
    mas[a[0]][a[1]] += 1

for i in range(101):
    for j in range(101):
        while mas[i][j] > 0:
            print(i, ", ", j, sep="")
            mas[i][j] -= 1
