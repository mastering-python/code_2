>>> import itertools

>>> list(itertools.compress(range(1000), [0, 1, 1, 1, 0, 1]))
[1, 2, 3, 5]


>>> primes = [0, 0, 1, 1, 0, 1, 0, 1]
>>> odd = [0, 1, 0, 1, 0, 1, 0, 1]
>>> numbers = ['zero', 'one', 'two', 'three', 'four', 'five']

# Primes:

>>> list(itertools.compress(numbers, primes))
['two', 'three', 'five']

# Odd numbers

>>> list(itertools.compress(numbers, odd))
['one', 'three', 'five']

# Odd primes

>>> list(itertools.compress(numbers, map(all, zip(odd, primes))))
['three', 'five']
