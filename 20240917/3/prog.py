tmp = number = int(input())

j = 0
while j < 3:
    i = 0
    while i < 3:
        print(number, "*", tmp, "=", end=" ")
        smile_test = tmp * number
        counter = 0
        while smile_test > 0:
            counter += smile_test % 10
            smile_test //= 10
        if counter == 6:
            print(":=)", end=" ")
        else:
            print(tmp * number, end=" ")
        tmp += 1
        i += 1
    print("\n", end="")
    tmp = number - j
    number += 1
    j += 1
