>>> import math
>>> import itertools

>>> def primes_complicated():
...     sieved = dict()
...     i = 2
...     
...     while True:
...         if i not in sieved:
...             yield i
...             sieved[i * i] = [i]
...         else:
...             for j in sieved[i]:
...                 sieved.setdefault(i + j, []).append(j)
...             del sieved[i]
...         
...         i += 1

>>> list(itertools.islice(primes_complicated(), 10))
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


>>> def primes_complex():
...     numbers = itertools.count(2)
...     while True:
...         yield (prime := next(numbers))
...         numbers = filter(prime.__rmod__, numbers)

>>> list(itertools.islice(primes_complex(), 10))
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

>>> def is_prime(number):
...     if number == 0 or number == 1:
...         return False
...     for modulo in range(2, number):
...         if not number % modulo:
...             return False
...     else:
...         return True

>>> def primes_simple():
...     for i in itertools.count():
...         if is_prime(i):
...             yield i

>>> list(itertools.islice(primes_simple(), 10))
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
