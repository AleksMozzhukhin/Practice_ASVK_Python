string = input()
ans = set()
for i in range(1, len(string)):
    if string[i].isalpha() and string[i - 1].isalpha():
        ans.add(string[i - 1:i + 1].lower())
print(len(ans))
