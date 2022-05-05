def primes(n):
    for i, prime in enumerate(prime_generator()):
        if i == n:
            return prime


def prime_generator():
    n = 2
    primes = set()
    while True:
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.add(n)
            yield n
        n += 1

