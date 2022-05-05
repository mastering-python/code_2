>>> some_user_input = '123abc'
>>> try:
...     value = int(some_user_input)
... except:
...     pass


>>> some_user_input = '123abc'
>>> try:
...     value = int(some_user_input)
... except ValueError:
...     pass


>>> import logging

>>> some_user_input = '123abc'
>>> try:
...     value = int(some_user_input)
... except Exception as exception:
...     logging.exception('Uncaught: {exception!r}')


>>> some_user_input_a = '123'
>>> some_user_input_b = 'abc'
>>> try:
...     value = int(some_user_input_a)
...     value += int(some_user_input_b)
... except:
...     value = 0


>>> try:
...     1 / 0  # Raises ZeroDivisionError
... except ZeroDivisionError:
...     print('Got zero division error')
... except Exception as exception:
...     print(f'Got unexpected exception: {exception}')
... except BaseException as exception:
...     # Base exceptions are a special case for keyboard
...     # interrupts and a few other exceptions that are not
...     # technically errors.
...     print(f'Got base exception: {exception}')
... else:
...     print('No exceptions happened, we can continue')
... finally:
...     # Useful cleanup functions such as closing a file
...     print('This code is _always_ executed')
Got zero division error
This code is _always_ executed

