>>> from os import *
>>> from asyncio import *

>>> assert wait



>>> from os import path
>>> from asyncio import wait

>>> assert wait



>>> import os
>>> import asyncio

>>> assert asyncio.wait
>>> assert os.path


>>> import concurrent.futures

>>> assert concurrent.futures.wait



>>> def spam(eggs, *args, **kwargs):
...     for arg in args:
...         eggs += arg
...     for extra_egg in kwargs.get('extra_eggs', []):
...         eggs += extra_egg
...     return eggs

>>> spam(1, 2, 3, extra_eggs=[4, 5])
15


>>> def sum_ints(*args):
...     total = 0
...     for arg in args:
...         total += arg
...     return total

>>> sum_ints(1, 2, 3, 4, 5)
15
