def compare(a, b):
    if a != b and a[0] <= b[0] and a[1] <= b[1] and a[2] <= b[2]:
        return False
    else:
        return True


triples = []
while t := input():
    triples.append(list(eval(t)))

sorted_triples = []
while triples:
    for i in triples:
        if all(compare(sorted(i), sorted(j)) for j in triples):
            sorted_triples.append(triples.pop(triples.index(i)))
            break
for i in sorted_triples:
    print(*i, sep=", ")
