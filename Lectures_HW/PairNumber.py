pairs = set()
words = []
while s := input().split():
    words += s
for i in range(1, len(words)):
    pairs.add((frozenset(words[i-1:i+1])))
print(len(pairs))
