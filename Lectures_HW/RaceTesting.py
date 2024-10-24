def speed(path, stops, times):
    cur_stop = 0
    tmp = stops[cur_stop]
    summ = 0
    for i in path:
        if tmp > 0:
            summ += i
            tmp -= 1
        else:
            try:
                yield summ / times[cur_stop]
                cur_stop += 1
                tmp = stops[cur_stop % (len(stops))]-1
                summ = i
            except IndexError:
                break

    yield summ / times[cur_stop % (len(times))]


print(*list(speed([2, 3, 4] * 11, [3, 4, 5], [1, 2, 4, 8] * 3)))
