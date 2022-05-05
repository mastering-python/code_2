# Adding default imports

>>> from pprint import pprint as pp
>>> from pprint import pformat as pf

>>> pp(dict(spam=0xA, eggs=0xB))
{'eggs': 11, 'spam': 10}
>>> pf(dict(spam=0xA, eggs=0xB))
"{'eggs': 11, 'spam': 10}"


# Modifying prompt

>>> if True:
...     print('Hello!')
Hello!

>>> import sys

>>> sys.ps1 = '> '
>>> sys.ps2 = '. '

# With modified prompt

> if True:
.     print('Hello!')
Hello!
