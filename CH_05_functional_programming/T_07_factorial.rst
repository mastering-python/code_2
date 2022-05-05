>>> import operator
>>> import functools

>>> functools.reduce(operator.mul, range(1, 5))
24

------------------------------------------------------------------------------

>>> from operator import mul

>>> mul(mul(mul(1, 2), 3), 4)
24

------------------------------------------------------------------------------

>>> import operator

>>> def reduce(function, iterable):
...     print(f'iterable={iterable}')
...     # Fetch the first item to prime `result`
...     result, *iterable = iterable
...
...     for item in iterable:
...         old_result = result
...         result = function(result, item)
...         print(f'{old_result} * {item} = {result}')
...
...     return result

>>> iterable = list(range(1, 5))
>>> iterable
[1, 2, 3, 4]

>>> reduce(operator.mul, iterable)
iterable=[1, 2, 3, 4]
1 * 2 = 2
2 * 3 = 6
6 * 4 = 24
24

------------------------------------------------------------------------------

>>> import operator

>>> iterable = range(1, 5)

# The initial values:

>>> a, b, *iterable = iterable
>>> a, b, iterable
(1, 2, [3, 4])

# First run

>>> a = operator.mul(a, b)
>>> b, *iterable = iterable
>>> a, b, iterable
(2, 3, [4])

# Second run

>>> a = operator.mul(a, b)
>>> b, *iterable = iterable
>>> a, b, iterable
(6, 4, [])

# Third and last run

>>> a = operator.mul (a, b)
>>> a
24

------------------------------------------------------------------------------

>>> import operator
>>> import collections

>>> iterable = collections.deque(range(1, 5))

>>> value = iterable.popleft()
>>> while iterable:
...     value = operator.mul(value, iterable.popleft())

>>> value
24

