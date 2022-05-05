>>> functions = [lambda: i for i in range(3)]

>>> for function in functions:
...     print(function(), end=', ')
2, 2, 2,


>>> from functools import partial

>>> functions = [partial(lambda x: x, i) for i in range(3)]

>>> for function in functions:
...     print(function(), end=', ')
0, 1, 2,
