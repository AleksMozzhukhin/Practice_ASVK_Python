mas = list(eval(input()))
for i in range(len(mas)):
    for j in range(len(mas)):
        if (mas[i] ** 2) % 100 < (mas[j] ** 2) % 100:
            mas[i], mas[j] = mas[j], mas[i]
print(mas)
