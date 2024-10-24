import itertools

length=int(input())
print(*sorted(list(filter(lambda x: x.count("TOR")==2, (''.join(i) for i in itertools.product('TOR', repeat=length))))), sep=", ")