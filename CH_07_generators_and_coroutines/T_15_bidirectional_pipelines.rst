>>> from coroutine_decorator import coroutine


>>> lines = 'some old text', 'really really old', 'old old old'

>>> @coroutine
... def replace(search, replace):
...     while True:
...         item = yield
...         print(item.replace(search, replace))


>>> old_replace = replace('old', 'new')
>>> for line in lines:
...     old_replace.send(line)
some new text
really really new
new new new

------------------------------------------------------------------------------

>>> @coroutine
... def replace(search, replace):
...     while True:
...         item = yield
...         yield item.replace(search, replace)


>>> old_replace = replace('old', 'new')
>>> for line in lines:
...     old_replace.send(line)
'some new text'
'new new new'

------------------------------------------------------------------------------

>>> @coroutine
... def replace(search, replace):
...     item = yield
...     while True:
...         item = yield item.replace(search, replace)


>>> old_replace = replace('old', 'new')
>>> for line in lines:
...     old_replace.send(line)
'some new text'
'really really new'
'new new new'

------------------------------------------------------------------------------

>>> @coroutine
... def replace(target, search, replace):
...     while True:
...         target.send((yield).replace(search, replace))

# Print will print the items using the provided formatstring

>>> @coroutine
... def print_(formatstring):
...     count = 0
...     while True:
...         count += 1
...         print(count, formatstring.format((yield)))

# Tee multiplexes the items to multiple targets

>>> @coroutine
... def tee(*targets):
...     while True:
...         item = yield
...         for target in targets:
...             target.send(item)


# Because we wrap the results we need to work backwards from the
inner layer to the outer layer.

# First, create a printer for the items:

>>> printer = print_('print: {}')

# Create replacers that send the output to the printer

>>> old_replace = replace(printer, 'old', 'new')
>>> current_replace = replace(printer, 'old', 'current')

# Send the input to both replacers

>>> branch = tee(old_replace, current_replace)

# Send the data to the tee routine for processing

>>> for line in lines:
...     branch.send(line)
1 print: some new text
2 print: some current text
3 print: really really new
4 print: really really current
5 print: new new new
6 print: current current current
