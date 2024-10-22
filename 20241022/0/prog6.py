def travel(n):
    yield from ["По кочкам"]*n
    return "и в яму"


def travelwlap(n):
    s = yield from travel(n)
    yield s


print(list(travelwlap(4)))
