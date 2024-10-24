def nonprime(n=0):
    max_prime = 100
    list_numbers = [True for i in range(max_prime + 1)]
    list_numbers[0] = list_numbers[1] = False
    list_primes = []
    current_number = 2
    if n == 0:
        yield 1
    while True:
        for i in range(current_number, max_prime + 1):
            if not list_numbers[i]:
                if i > n:
                    yield i
            else:
                list_primes.append(i)
                for not_primes in range(i * i, max_prime + 1, i):
                    list_numbers[not_primes] = False
        current_number = max_prime
        max_prime *= 2
        list_numbers += [True for j in range(max_prime // 2)]
        for found_prime in list_primes:
            for not_primes in range(max(found_prime * found_prime, (current_number // found_prime + 1) * found_prime),
                                    max_prime + 1, found_prime):
                list_numbers[not_primes] = False
        current_number += 1
