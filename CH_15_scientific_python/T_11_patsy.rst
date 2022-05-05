>>> import patsy
>>> import numpy as np

>>> array = np.arange(2, 6)

>>> data = dict(a=array, b=array, c=array)
>>> patsy.dmatrix('a + np.square(b) + np.power(c, 3)', data)
DesignMatrix with shape (4, 4)
  Intercept  a  np.square(b)  np.power(c, 3)
          1  2             4               8
          1  3             9              27
          1  4            16              64
          1  5            25             125
  Terms:
    'Intercept' (column 0)
    'a' (column 1)
    'np.square(b)' (column 2)
    'np.power(c, 3)' (column 3)
