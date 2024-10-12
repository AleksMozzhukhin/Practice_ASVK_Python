def f(r1, r2, r):
    if (r1[0] - r[0]) * (r2[1] - r1[1]) - (r2[0] - r1[0]) * (r1[1] - r[1]) > 0:
        return 1
    else:
        return -1


def in_triange(t, x):
    return f(t[1], t[2], x) == f(t[0], t[1], x) and f(t[2], t[0], x) == f(t[0], t[1], x)

s = input()
lst = []
while s := input():
    lst.append(eval(s))
n = len(lst)
for p1 in range(n):
    for p in range(n):
        if p == p1 or p == (p1 + 1) % n or p == (p1 + 2) % n:
            continue
        if in_triange((lst[p1], lst[(p1 + 1) % n], lst[(p1 + 2) % n]), lst[p]):
            print(False)
            exit()
print(True)