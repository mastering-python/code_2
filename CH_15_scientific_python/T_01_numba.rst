>>> import numpy
>>> import numba

>>> numbers = numpy.arange(500, dtype=numpy.int64)

>>> @numba.vectorize([numba.int64(numba.int64)])
... def add_one(x):
...     return x + 1

>>> numbers
array([  0,   1,   2, ..., 498, 499])

>>> add_one(numbers)
array([  1,   2,   3, ..., 499, 500])

