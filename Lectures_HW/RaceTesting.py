def speed(path, stops, times):
    from itertools import tee

    stops_dup = list(tee(stops, 2))
    times = iter(times)
    path = iter(path)
    tmp = next(stops_dup[0])
    summ = 0
    for i in path:
        if tmp > 0:
            summ += i
            tmp -= 1
        else:
            try:
                yield summ / next(times)
                try:
                    tmp = next(stops_dup[0]) - 1
                except StopIteration:
                    stops_dup = tee(stops_dup[1], 2)
                    tmp = next(stops_dup[0]) - 1
                summ = i
            except IndexError:
                break
    yield summ / next(times)
