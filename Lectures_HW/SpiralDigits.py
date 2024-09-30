length, height = eval(input())
counter = 0
a = [[0 for i in range(length)] for j in range(height)]
# print(*a)
cur_num = 0
while counter < max(length, height) // 2:
    # print(counter)
    for i in range(counter, length - counter):
        a[counter][i] += cur_num % 10
        cur_num += 1
    for i in range(counter + 1, height - counter):
        a[i][length-counter-1] += cur_num % 10
        cur_num += 1
    for i in range(length-counter-2, counter-1, -1):
        a[height-counter-1][i] += cur_num % 10
        cur_num += 1
    for i in range(height-counter-2, counter, -1):
        a[i][counter] += cur_num % 10
        cur_num += 1
    counter += 1
    for i in range(height):
        for j in range(length):
            print(a[i][j], end=" ")
        print("")
    print("")
