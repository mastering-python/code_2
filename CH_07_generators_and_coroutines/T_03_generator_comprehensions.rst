>>> squares = (x ** 2 for x in range(4))

>>> squares
<generator object <genexpr> at 0x...>

>>> list(squares)
[0, 1, 4, 9]

------------------------------------------------------------------

>>> import itertools

>>> result = itertools.count()
>>> odd = (x for x in result if x % 2)
>>> sliced_odd = itertools.islice(odd, 5)
>>> list(sliced_odd)
[1, 3, 5, 7, 9]

------------------------------------------------------------------

>>> result = itertools.count()
>>> sliced_result = itertools.islice(result, 5)
>>> odd = (x for x in sliced_result if x % 2)
>>> list(odd)
[1, 3]
