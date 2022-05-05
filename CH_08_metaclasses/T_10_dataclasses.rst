>>> from T_10_dataclasses import Dataclass

>>> class Sandwich(metaclass=Dataclass):
...     spam: int
...     eggs: int = 3

>>> Sandwich(1, 2)
Sandwich(spam=1, eggs=2)

>>> sandwich = Sandwich(4)
>>> sandwich
Sandwich(spam=4, eggs=3)
>>> sandwich.eggs
3

>>> help(Sandwich.__init__)
Help on function __init__ in ...
<BLANKLINE>
__init__(spam: int, eggs: int = 3)
<BLANKLINE>

>>> Sandwich('a')
Traceback (most recent call last):
    ...
ValueError: invalid literal for int() with base 10: 'a'

>>> Sandwich('1234', 56.78)
Sandwich(spam=1234, eggs=56)
