>>> from coroutine_decorator import coroutine

>>> @coroutine
... def simple_coroutine():
...     print('Setting up the coroutine')
...     try:
...         while True:
...             item = yield
...             print('Got item:', item)
...     except GeneratorExit:
...         print('Normal exit')
...     except Exception as e:
...         print('Exception exit:', e)
...         raise
...     finally:
...         print('Any exit')

>>> active_coroutine = simple_coroutine()
Setting up the coroutine
>>> active_coroutine.send('from caller')
Got item: from caller
>>> active_coroutine.close()
Normal exit
Any exit

>>> active_coroutine = simple_coroutine()
Setting up the coroutine
>>> active_coroutine.throw(RuntimeError, 'caller sent an error')
Traceback (most recent call last):
    ...
RuntimeError: caller sent an error

>>> active_coroutine = simple_coroutine()
Setting up the coroutine
>>> try:
...     active_coroutine.throw(RuntimeError, 'caller sent an error')
... except RuntimeError as exception:
...     print('Exception:', exception)
Exception exit: caller sent an error
Any exit
Exception: caller sent an error
