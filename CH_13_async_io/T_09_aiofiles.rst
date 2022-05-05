>>> import asyncio
>>> import aiofiles

>>> async def main():
...     async with aiofiles.open('aiofiles.txt', 'w') as fh:
...         await fh.write('Writing to file')
...
...     async with aiofiles.open('aiofiles.txt', 'r') as fh:
...         async for line in fh:
...             print(line) 


>>> asyncio.run(main())
Writing to file
