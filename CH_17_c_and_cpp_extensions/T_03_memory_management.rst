>>> import ctypes

>>> class Point(ctypes.Structure):
...     _fields_ = ('x', ctypes.c_int), ('y', ctypes.c_int)

>>> class Vertex(ctypes.Structure):
...     _fields_ = ('c', Point), ('d', Point)

>>> a = Point(0, 1)
>>> b = Point(2, 3)
>>> a.x, a.y, b.x, b.y
(0, 1, 2, 3)

# Swap points a and b

>>> a, b = b, a
>>> a.x, a.y, b.x, b.y
(2, 3, 0, 1)

>>> v = Vertex()
>>> v.c = Point(0, 1)
>>> v.d = Point(2, 3)
>>> v.c.x, v.c.y, v.d.x, v.d.y
(0, 1, 2, 3)

# Swap points c and d

>>> v.c, v.d = v.d, v.c
>>> v.c.x, v.c.y, v.d.x, v.d.y
(2, 3, 2, 3)


# Regular Python version to illustrate the difference:

>>> import dataclasses

>>> @dataclasses.dataclass
... class Point:
...     x: int
...     y: int

>>> @dataclasses.dataclass
... class Vertex:
...     c: Point
...     d: Point

>>> a = Point(0, 1)
>>> b = Point(2, 3)
>>> a.x, a.y, b.x, b.y
(0, 1, 2, 3)

# Swap points a and b

>>> a, b = b, a
>>> a.x, a.y, b.x, b.y
(2, 3, 0, 1)

>>> v = Vertex(c = Point(0, 1), d = Point(2, 3))
>>> v.c.x, v.c.y, v.d.x, v.d.y
(0, 1, 2, 3)

# Swap points c and d

>>> v.c, v.d = v.d, v.c
>>> v.c.x, v.c.y, v.d.x, v.d.y
(2, 3, 0, 1)
