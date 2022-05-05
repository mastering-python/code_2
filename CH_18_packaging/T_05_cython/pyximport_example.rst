# python3

>>> import pyximport

>>> pyximport.install()
(None, <pyximport.pyximport.PyxImporter object at ...>)

>>> from T_05_cython import sum_of_squares

>>> sum_of_squares.sum_of_squares(10)
14
