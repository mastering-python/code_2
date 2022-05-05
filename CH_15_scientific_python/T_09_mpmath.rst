>>> N = 10
>>> x = 0.1

# Regular addition

>>> a = 0.0
>>> for _ in range(N):
...     a += x

>>> a
0.9999999999999999

# Using sum, the same result as addition

>>> sum(x for _ in range(N))
0.9999999999999999

#################################################################

# Sum using Python's optimized fsum:

>>> import math

>>> math.fsum(x for _ in range(N))
1.0

#################################################################

>>> import mpmath

# Increase the mpmath precision to 100 decimal places

>>> mpmath.mp.dps = 100
>>> y = mpmath.mpf('0.1')

# Using mpmath with addition:

>>> b = mpmath.mpf('0.0')
>>> for _ in range(N):
...     b += y

>>> b
mpf('1.00000000000000000000000000...00000000000000000000000014')

# Or a regular sum with mpmath:

>>> sum(y for _ in range(N))
mpf('1.00000000000000000000000000...00000000000000000000000014')
