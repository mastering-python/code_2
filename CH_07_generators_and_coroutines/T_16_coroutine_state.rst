>>> import itertools

>>> from coroutine_decorator import coroutine


>>> @coroutine
... def average():
...     total = yield
...     for count in itertools.count(start=1):
...         total += yield total / count

>>> averager = average()
>>> averager.send(20)
20.0
>>> averager.send(10)
15.0

------------------------------------------------------------------------------

>>> import itertools

>>> @coroutine
... def print_(formatstring):
...     while True:
...         print(formatstring.format((yield)))


>>> @coroutine
... def average(target):
...     total = 0
...     for count in itertools.count(start=1):
...         total += yield
...         target.send(total / count)

>>> printer = print_('{:.1f}')
>>> averager = average(printer)
>>> averager.send(20)
20.0
>>> averager.send(10)
15.0

------------------------------------------------------------------------------

>>> @coroutine
... def groupby():
...     # Fetch the first key and value and initialize the state
...     # variables
...     key, value = yield
...     old_key, values = key, []
...     while True:
...         # Store the previous value so we can store it in the
...         # list
...         old_value = value
...         if key == old_key:
...             key, value = yield
...         else:
...             key, value = yield old_key, values
...             old_key, values = key, []
...         values.append(old_value)


>>> grouper = groupby()
>>> grouper.send('a1')
>>> grouper.send('a2')
>>> grouper.send('a3')
>>> grouper.send('b1')
('a', ['1', '2', '3'])
>>> grouper.send('b2')
>>> grouper.send('a1')
('b', ['1', '2'])
>>> grouper.send('a2')
>>> grouper.send((None, None))
('a', ['1', '2'])

------------------------------------------------------------------------------

>>> @coroutine
... def print_(formatstring):
...     while True:
...         print(formatstring.format(*(yield)))

>>> @coroutine
... def groupby(target):
...     old_key = None
...     while True:
...         key, value = yield
...         if old_key != key:
...             # A different key means a new group so send the
...             # previous group and restart the cycle.
...             if old_key and values:
...                 target.send((old_key, values))
...             values = []
...             old_key = key
...         values.append(value)


>>> grouper = groupby(print_('group: {}, values: {}'))
>>> grouper.send('a1')
>>> grouper.send('a2')
>>> grouper.send('a3')
>>> grouper.send('b1')
group: a, values: ['1', '2', '3']
>>> grouper.send('b2')
>>> grouper.send('a1')
group: b, values: ['1', '2']
>>> grouper.send('a2')
>>> grouper.send((None, None))
group: a, values: ['1', '2']

