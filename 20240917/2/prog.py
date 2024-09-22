answer = 0
while (tmp_num := int(input())) > 0:
    answer += tmp_num
    if answer > 21:
        print(answer)
        break
else:
    print(tmp_num)
