>>> import ctypes


>>> TenNumbers = 10 * ctypes.c_double
>>> numbers = TenNumbers()
>>> numbers[0]
0.0

------------------------------------------------------------------------------

>>> class ComplexStructure(ctypes.Structure):
...     _fields_ = [
...         ('some_int', ctypes.c_int),
...         ('some_double', ctypes.c_double),
...         ('some_char', ctypes.c_char),
...         ('some_string', ctypes.c_char_p),
...     ]


>>> GrossComplexStructures = 144 * ComplexStructure 
>>> complex_structures = GrossComplexStructures()

>>> complex_structures[10].some_double = 123
>>> complex_structures[10]
<__main__.ComplexStructure object at ...>
>>> complex_structures
<__main__.ComplexStructure_Array_144 object at ...>

------------------------------------------------------------------------------

>>> TenNumbers = 10 * ctypes.c_double
>>> numbers = TenNumbers()
>>> ctypes.resize(numbers, 11 * ctypes.sizeof(ctypes.c_double))
>>> ctypes.resize(numbers, 10 * ctypes.sizeof(ctypes.c_double))
>>> ctypes.resize(numbers, 9 * ctypes.sizeof(ctypes.c_double))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: minimum size is 80
>>> numbers[:5] = range(5)
>>> numbers[:]
[0.0, 1.0, 2.0, 3.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0]

