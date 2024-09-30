from sys import stdin
matr = []
for line in stdin:
    matr.append(eval(line))

for i in range(len(matr)):
    j = i
    print(*(matr[i][j] for j in range(i + 1)), sep=',', end='')
    if i != 0:
        print(',', end='')
    print(*(matr[k][j] for k in range(j - 1, -1, -1)), sep=',', end='')
    print("")
