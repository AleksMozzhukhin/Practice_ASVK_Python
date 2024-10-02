def divdigit(n):
    count = 0
    string=str(n)
    for i in range(len(str(n))):
        if string[i] != '0' and n % int(string[i]) == 0:
            count += 1
    return count