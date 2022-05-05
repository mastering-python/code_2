>>> import time
>>> import asyncio

>>> def normal_sleep():
...     print('before sleep')
...     time.sleep(1)
...     print('after sleep')


>>> def normal_sleeps(n):
...     for _ in range(n):
...         normal_sleep()


# Normal execution

>>> start = time.time()
>>> normal_sleeps(2)
before sleep
after sleep
before sleep
after sleep
>>> print(f'duration: {time.time() - start:.0f}')
duration: 2

##################################################################

>>> async def asyncio_sleep():
...     print('before sleep')
...     await asyncio.sleep(1)
...     print('after sleep')


>>> async def asyncio_sleeps(n):
...     coroutines = []
...     for _ in range(n):
...         coroutines.append(asyncio_sleep())
...
...     await asyncio.gather(*coroutines)

>>> start = time.time()
>>> asyncio.run(asyncio_sleeps(2))
before sleep
before sleep
after sleep
after sleep
>>> print(f'duration: {time.time() - start:.0f}')
duration: 1

