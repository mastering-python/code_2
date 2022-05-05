>>> import asyncio


>>> class AsyncGenerator:
...     def __init__(self, iterable):
...         self.iterable = iterable
...
...     async def __aiter__(self):
...         for item in self.iterable:
...             yield item


>>> async def main():
...     async_generator = AsyncGenerator([4, 2])
...
...     async for item in async_generator:
...         print(f'Got item: {item}')

>>> asyncio.run(main())
Got item: 4
Got item: 2
