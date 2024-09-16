cur_len, max_len = 1, 1
prev_num = int(input())
while cur_num := int(input()):
    if cur_num >= prev_num:
        cur_len += 1
    else:
        max_len = max(max_len, cur_len)
        cur_len = 1
    prev_num = cur_num
max_len = max(max_len, cur_len)
print(max_len)