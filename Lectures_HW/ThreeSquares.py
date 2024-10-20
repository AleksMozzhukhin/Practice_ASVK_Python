seq = set(eval(input()))
set_squares = set()
max_s = max(seq)
tmp_0_0 = int(max_s ** 0.5) + 1
for i in range(1, tmp_0_0):
    tmp1 = i * i
    tmp_1_0 = int((max_s - tmp1) ** 0.5) + 1
    for j in range(i, tmp_1_0):
        tmp2 = j * j
        tmp_2_0 = int((max_s - tmp1 - tmp2) ** 0.5) + 1
        for k in range(j, tmp_2_0):
            set_squares.add((tmp1 + tmp2 + k * k))
print(len(seq & set_squares))
