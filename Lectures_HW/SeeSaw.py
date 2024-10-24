def seesaw(sequence):
    even_elements = []
    odd_elements = []
    for i in sequence:
        if i % 2 == 0:
            even_elements.append(i)
        else:
            odd_elements.append(i)
    i = 0
    for i in range(min(len(odd_elements), len(even_elements))):
        yield even_elements[i]
        yield odd_elements[i]
    if len(odd_elements) > len(even_elements):
        if i==0:
            yield from odd_elements[i:]
        else:
            yield from odd_elements[i+1:]
    else:
        if i == 0:
            yield from even_elements[i:]
        else:
            yield from even_elements[i + 1:]
