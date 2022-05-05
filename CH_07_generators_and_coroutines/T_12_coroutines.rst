>>> def generator():
...     value = yield 'value from generator'
...     print('Generator received:', value)
...     yield f'Previous value: {value!r}'

>>> g = generator()
>>> print('Result from generator:', next(g))
Result from generator: value from generator

>>> print(g.send('value from caller'))
Generator received: value from caller
Previous value: 'value from caller'
