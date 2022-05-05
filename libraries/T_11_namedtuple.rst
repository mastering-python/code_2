>>> import collections

>>> Point = collections.namedtuple('Point', ['x', 'y', 'z'])
>>> point_a = Point(1, 2, 3)
>>> point_a
Point(x=1, y=2, z=3)

>>> point_b = Point(x=4, z=5, y=6)
>>> point_b
Point(x=4, y=6, z=5)

------------------------------------------------------------------------------

>>> x, y, z = point_a
>>> print(f'X: {x}, Y: {y}, Z: {z}')
X: 1, Y: 2, Z: 3
>>> print('X: {}, Y: {}, Z: {}'.format(*point_b))
X: 4, Y: 6, Z: 5
>>> print('X: %d, Y: %d, Z: %d' % point_b)
X: 4, Y: 6, Z: 5
>>> print(f'X: {point_a.x}')
X: 1
