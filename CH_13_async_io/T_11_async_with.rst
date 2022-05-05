>>> import asyncio


>>> class AsyncContextManager:
...     async def __aenter__(self):
...         print('Hi :)')
...
...     async def __aexit__(self, exc_type, exc_value, traceback):
...         print('Bye :(')


>>> async def main():
...     async_context_manager = AsyncContextManager()
...
...     print('Before with')
...     async with async_context_manager:
...         print('During with')
...     print('After with')

>>> asyncio.run(main())
Before with
Hi :)
During with
Bye :(
After with
