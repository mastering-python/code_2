>>> from _libc import libc
>>> import ctypes

>>> class ComplexStructure(ctypes.Structure):
...     _fields_ = [
...         ('some_int', ctypes.c_int),
...         ('some_double', ctypes.c_double),
...         ('some_char', ctypes.c_char),
...         ('some_string', ctypes.c_char_p),
...     ]
... 
>>> structure = ComplexStructure(123, 456.789, b'x', b'abc')
>>> structure.some_int
123
>>> structure.some_double
456.789
>>> structure.some_char
b'x'
>>> structure.some_string
b'abc'
