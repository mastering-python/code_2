>>> import asyncio


>>> class SomeClass:
...     def __init__(self, *args, **kwargs):
...         print('Sync init')
...
...     async def init(self, *args, **kwargs):
...         print('Async init')
...
...     @classmethod
...     async def create(cls, *args, **kwargs):
...         # Create an instance of `SomeClass` which calls the
...         # sync init: `SomeClass.__init__(*args, **kwargs)`
...         self = cls(*args, **kwargs)
...         # Now we can call the async init:
...         await self.init(*args, **kwargs)
...         return self
...
...     async def close(self):
...         print('Async destructor')
...
...     def __del__(self):
...         print('Sync destructor')


>>> async def main():
...     # Note that we use `SomeClass.create()` instead of
...     # `SomeClass()` so we also run `SomeClass().init()`
...     some_class = await SomeClass.create()
...     print('Using the class here')
...     await some_class.close()
...     del some_class

>>> asyncio.run(main())
Sync init
Async init
Using the class here
Async destructor
Sync destructor
