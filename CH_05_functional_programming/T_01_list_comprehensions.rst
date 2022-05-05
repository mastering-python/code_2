>>> squares = [x ** 2 for x in range(10)]
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

------------------------------------------------------------------------------

>>> odd_squares = [x ** 2 for x in range(10) if x % 2]
>>> odd_squares
[1, 9, 25, 49, 81]

------------------------------------------------------------------------------

>>> def square(x):
...     return x ** 2

>>> def odd(x):
...     return x % 2

>>> squares = list(map(square, range(10)))
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

>>> odd_squares = list(filter(odd, map(square, range(10))))
>>> odd_squares
[1, 9, 25, 49, 81]

------------------------------------------------------------------------------

>>> import os

>>> directories = filter(os.path.isdir, os.listdir('.'))

# Versus:

>>> directories = [x for x in os.listdir('.') if os.path.isdir(x)]

------------------------------------------------------------------------------

>>> odd_squares = []
>>> for x in range(10):
...     if x % 2:
...         odd_squares.append(x ** 2)

>>> odd_squares
[1, 9, 25, 49, 81]

------------------------------------------------------------------------------

# List comprehension

>>> [x // 2 for x in range(3)]
[0, 0, 1]

# Set comprehension

>>> numbers = {x // 2 for x in range(3)}
>>> sorted(numbers)
[0, 1]

------------------------------------------------------------------------------

>>> import random

>>> [random.random() for _ in range(10) if random.random() >= 0.5]
... # doctest: +SKIP
[0.5211948104577864, 0.650010512129705, 0.021427316545174158]

------------------------------------------------------------------------------

>>> import random

>>> numbers = [random.random() for _ in range(10)] # doctest: +SKIP

>>> [x for x in numbers if x >= 0.5] # doctest: +SKIP
[0.715510247827078, 0.8426277505519564, 0.5071133900377911]

------------------------------------------------------------------------------

>>> import random

>>> [x for x in [random.random() for _ in range(10)] if x >= 0.5]
... # doctest: +SKIP

------------------------------------------------------------------------------

>>> import random

>>> [x for _ in range(10) for x in [random.random()] if x >= 0.5]
... # doctest: +SKIP

------------------------------------------------------------------------------

>>> [(x, y) for x in range(3) for y in range(3, 5)]
[(0, 3), (0, 4), (1, 3), (1, 4), (2, 3), (2, 4)]

------------------------------------------------------------------------------

>>> results = []
>>> for x in range(3):
...     for y in range(3, 5):
...         results.append((x, y))
...
>>> results
[(0, 3), (0, 4), (1, 3), (1, 4), (2, 3), (2, 4)]

------------------------------------------------------------------------------

>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]

>>> reshaped_matrix = [
...     [
...         [y for x in matrix for y in x][i * len(matrix) + j]
...         for j in range(len(matrix))
...     ]
...     for i in range(len(matrix[0]))
... ]

>>> import pprint

>>> pprint.pprint(reshaped_matrix, width=40)
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9],
 [10, 11, 12]]

