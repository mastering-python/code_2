>>> import time
>>> import datetime
>>> import contextlib

# Context manager that shows how long a context was active

>>> @contextlib.contextmanager
... def timer(name):
...     start_time = datetime.datetime.now()
...     yield
...     stop_time = datetime.datetime.now()
...     print('%s took %s' % (name, stop_time - start_time))

>>> with timer('basic timer'):
...     time.sleep(0.1)
basic timer took 0:00:00.1...

# Write standard print output to a file temporarily

>>> @contextlib.contextmanager
... def write_to_log(name):
...     with open(f'{name}.txt', 'w') as fh:
...         with contextlib.redirect_stdout(fh):
...             with timer(name):
...                 yield

# Using as a decorator also works in addition to with-statements

>>> @write_to_log('some_name')
... def some_function():
...     print('This will be written to `some_name.txt`')

>>> some_function()

------------------------------------------------------------------------------

>>> import contextlib


>>> @contextlib.contextmanager
... def write_to_log(name):
...     with contextlib.ExitStack() as stack:
...         fh = stack.enter_context(open(f'{name}.txt', 'w'))
...         stack.enter_context(contextlib.redirect_stdout(fh))
...         stack.enter_context(timer(name))
...         yield

>>> @write_to_log('some_name')
... def some_function():
...     print('This will be written to `some_name.txt`')

>>> some_function()

------------------------------------------------------------------------------

>>> import contextlib

>>> with contextlib.ExitStack() as stack:
...     fh = stack.enter_context(open('file.txt', 'w'))
...     # Move the context(s) to a new ExitStack
...     new_stack = stack.pop_all()

>>> bytes_written = fh.write('fh is still open')

# After closing we can't write anymore

>>> new_stack.close()
>>> fh.write('cant write anymore')
Traceback (most recent call last):
    ...
ValueError: I/O operation on closed file.
