>>> import time
>>> import asyncio


>>> def executor_sleep():
...     print('before sleep')
...     time.sleep(1)
...     print('after sleep')


>>> async def executor_sleeps(n):
...     loop = asyncio.get_running_loop()
...     futures = []
...     for _ in range(n):
...         future = loop.run_in_executor(None, executor_sleep)
...         futures.append(future)
...
...     await asyncio.gather(*futures)

>>> start = time.time()
>>> asyncio.run(executor_sleeps(2))
before sleep
before sleep
after sleep
after sleep
>>> print(f'duration: {time.time() - start:.0f}')
duration: 1
