def primes():
    known_primes = []
    candidate = 2
    while True:
        is_prime = True
        for d in known_primes:
            if candidate % d == 0:
                is_prime = False
                break
            if d > candidate**0.5:
                break

        if is_prime:
            known_primes.append(candidate)
            yield candidate
        candidate += 1

# n = primes()
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
obj = primes()
for e in obj:
    print('>>>', e)