>>> import itertools

>>> list(itertools.combinations(range(3), 2))
[(0, 1), (0, 2), (1, 2)]

------------------------------------------------------------------------------

>>> import itertools

>>> list(itertools.combinations_with_replacement(range(3), 2))
[(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]

------------------------------------------------------------------------------

>>> import itertools

>>> def powerset(iterable):
...     return itertools.chain.from_iterable(
...         itertools.combinations(iterable, i)
...         for i in range(len(iterable) + 1))
>>> list(powerset(range(3)))
[(), (0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2)]
