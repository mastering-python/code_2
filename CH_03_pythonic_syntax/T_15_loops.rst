>>> my_range = range(5)
>>> i = 0
>>> while i < len(my_range):
...     item = my_range[i]
...     print(i, item, end=', ')
...     i += 1
0 0, 1 1, 2 2, 3 3, 4 4,


>>> my_range = range(5)
>>> for item in my_range:
...     print(item, end=', ')
0, 1, 2, 3, 4,

>>> for i, item in enumerate(my_range):
...     print(i, item, end=', ')
0 0, 1 1, 2 2, 3 3, 4 4,

>>> my_range = range(5)
>>> [(i, item) for i, item in enumerate(my_range)]
[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
