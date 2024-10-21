words_length = int(input())
text = ""
while s := input():
    text += ''.join(letter if letter.isalpha() else " " for letter in s)

words_by_entry = {}
for i in text.split():
    if len(i) == words_length:
        if i not in words_by_entry:
            words_by_entry[i] = 1
        else:
            words_by_entry[i] += 1
max_words_count = max(words_by_entry.values())
print(*[words for words, count in words_by_entry.items() if count == max_words_count])
