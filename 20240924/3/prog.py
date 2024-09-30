matrix1 = [list(eval(input()))]
n = len(matrix1[0])
for i in range(1, n):
    matrix1.append(list(eval(input())))
matrix2 = []
for i in range(n):
    matrix2.append(list(eval(input())))
for i in range(n):
    ans = [0 for k in range(n)]
    for j in range(n):  # for k in range(n):
        for k in range(n):
            ans[j] += (matrix1[i][k] * matrix2[k][j])
    print(*(k for k in ans), sep=",", end="")
    print("")
