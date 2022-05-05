Note: missing_ok was added in Python 3.8

>>> import pathlib

>>> pathlib.Path('bpython.txt').unlink(missing_ok=True)

>>> with open('bpython.txt', 'a') as fh:
...     fh.write('x')
...
1
>>> with open('bpython.txt') as fh:
...     print(fh.read())
...
x
>>> sandwich = dict(spam=2, eggs=1, sausage=1)

>>> with open('bpython.txt', 'a') as fh:
...     fh.write('x')
...
1
>>> with open('bpython.txt') as fh:
...     print(fh.read())
...
xx
>>>
