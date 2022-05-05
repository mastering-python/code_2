>>> from sympy import *

>>> init_printing(use_unicode=True)
>>> x, y, z = symbols('x y z')

>>> integral = Integral(x * cos(x), x)
>>> integral
⌠
⎮ x⋅cos(x) dx
⌡
>>> integral.doit()
x⋅sin(x) + cos(x)
