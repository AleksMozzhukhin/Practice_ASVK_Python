ans = None
while mixed_string:=input():
    for i in mixed_string.split():
        if i.removeprefix('-').isdecimal():
            if ans is None:
                ans = int(i)
            elif int(i) > ans:
                ans = int(i)
if ans is None:
    print(0)
else:
    print(ans)
