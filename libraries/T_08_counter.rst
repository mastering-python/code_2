>>> import collections

>>> counter = collections.Counter('eggs')
>>> for character in 'eggs':
...     print(f'Count for {character}: {counter[character]}')
Count for e: 1
Count for g: 2
Count for g: 2
Count for s: 1

------------------------------------------------------------------------------

>>> import math
>>> import collections

>>> counter = collections.Counter()
>>> for i in range(0, 100000):
...    counter[math.sqrt(i) // 25] += 1

>>> for key, count in counter.most_common(5):
...     print(f'{key}: {count}')
11.0: 14375
10.0: 13125
9.0: 11875
8.0: 10625
12.0: 10000

------------------------------------------------------------------------------

>>> import collections

>>> def print_sorted(counter):
...     sorted_characters = sorted(counter.elements())
...     print(''.join(sorted_characters))

>>> eggs = collections.Counter('eggs')
>>> spam = collections.Counter('spam')
>>> print_sorted(eggs)
eggs
>>> print_sorted(spam)
amps
>>> print_sorted(eggs & spam)
s
>>> print_sorted(spam & eggs)
s
>>> print_sorted(eggs - spam)
egg
>>> print_sorted(spam - eggs)
amp
>>> print_sorted(eggs + spam)
aeggmpss
>>> print_sorted(spam + eggs)
aeggmpss
>>> print_sorted(eggs | spam)
aeggmps
>>> print_sorted(spam | eggs)
aeggmps
