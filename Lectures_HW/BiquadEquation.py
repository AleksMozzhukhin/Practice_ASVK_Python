a, b, c = eval(input())
d = b ** 2 - 4 * a * c
answer = []
if a == 0:
    if b == 0:
        if c == 0:
            answer.append(-1)
        else:
            answer.append(0)
    elif (-c / b) > 0:
        answer.append((-c / b) ** 0.5)
        answer.append(-(-c / b) ** 0.5)
    else:
        answer.append(0)
elif d < 0:
    answer.append(0)
elif d == 0:
    if (-b / 2 * a) <= 0:
        answer.append(0)
    else:
        answer.append((-b / 2 * a) ** 0.5)
        answer.append(-(-b / 2 * a) ** 0.5)
else:
    x_1 = (-b + d ** 0.5) / (2 * a)
    x_2 = (-b - d ** 0.5) / (2 * a)
    if x_1 < 0 and x_2 < 0:
        answer.append(0)
    if x_1 > 0:
        answer.append(x_1 ** 0.5)
        answer.append(-(x_1 ** 0.5))
    elif x_1 == 0:
        answer.append(0)
    if x_2 > 0:
        answer.append(x_2 ** 0.5)
        answer.append(-(x_2 ** 0.5))
    elif x_2 == 0:
        answer.append(0)
print(*sorted(answer), sep=" ")
