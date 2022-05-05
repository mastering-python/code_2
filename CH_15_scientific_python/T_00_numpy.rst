# A commonly used shorthand for numpy is np

>>> import numpy as np

# Generate an array of numbers from 0 up to 1 million

>>> a = np.arange(1000000)
>>> a
array([        0,         1, ..., 999998, 999999])

# Change the shape (still references the same data) to a
2-dimensional 1000x1000 array

>>> b = a.reshape((1000, 1000))
>>> b
array([[     0,      1,      2, ...,    997,    998,    999],
       [  1000,   1001,   1002, ...,   1997,   1998,   1999],
       ...,
       [998000, 998001, 998002, ..., 998997, 998998, 998999],
       [999000, 999001, 999002, ..., 999997, 999998, 999999]])

# The first row of the matrix

>>> b[0]
array([  0,   1,   2,   3, ..., 995, 996, 997, 998, 999])

# The first column of the matrix

>>> b[:, 0]
array([     0,   1000,   2000,   ..., 997000, 998000, 999000])

# Row 10 up to 12, the even columns between 20 and 30

>>> b[10:12, 20:30:2]
array([[10020, 10022, 10024, 10026, 10028],
       [11020, 11022, 11024, 11026, 11028]])

# Row 10, columns 5 up to 10:

>>> b[10, 5:10]
array([10005, 10006, 10007, 10008, 10009])

# Alternative syntax for the last slice

>>> b[10][5:10]
array([10005, 10006, 10007, 10008, 10009])

##################################################################

>>> b[0] *= 10
>>> b[:, 0] *= 20

>>> a
array([     0,     10,     20, ..., 999997, 999998, 999999])
>>> b[0:2]
array([[    0,    10,    20, ...,  9970,  9980,  9990],
       [20000,  1001,  1002, ...,  1997,  1998,  1999]])

##################################################################

>>> a = list(range(10000))

>>> def dot(xs, ys):
...     total = 0
...     for x, y in zip(xs, ys):
...         total += x * y
...     return total

>>> dot(a, a)
333283335000

>>> np.dot(a, a)
333283335000
