>>> class Open:
...     def __init__(self, filename, mode):
...         self.filename = filename
...         self.mode = mode
...
...     def __enter__(self):
...         self.handle = open(self.filename, self.mode)
...         return self.handle
...
...     def __exit__(self, exc_type, exc_val, exc_tb):
...         self.handle.close()


>>> with Open('test.txt', 'w') as fh:
...     print('Our test is complete!', file=fh)

-----------------------------------------------------------------

>>> import contextlib


>>> @contextlib.contextmanager
... def open_context_manager(filename, mode='r'):
...     fh = open(filename, mode)
...     yield fh
...     fh.close()


>>> with open_context_manager('test.txt', 'w') as fh:
...     print('Our test is complete!', file=fh)

------------------------------------------------------------------------------

>>> import contextlib

>>> with contextlib.closing(open('test.txt', 'a')) as fh:
...     print('Yet another test', file=fh)

------------------------------------------------------------------------------

>>> @contextlib.contextmanager
... def debug(name):
...     print(f'Debugging {name}:')
...     yield
...     print(f'Finished debugging {name}')


>>> @debug('spam')
... def spam():
...     print('This is the inside of our spam function')

>>> spam()
Debugging spam:
This is the inside of our spam function
Finished debugging spam
