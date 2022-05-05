import asyncio


@asyncio.coroutine
def main():
    print('Hello from main')
    yield from asyncio.sleep(1)


loop = asyncio.new_event_loop()
loop.run_until_complete(main())
loop.close()

#################################################################

import asyncio


async def main():
    print('Hello from main')
    await asyncio.sleep(1)


loop = asyncio.new_event_loop()
loop.run_until_complete(main())
loop.close()

#################################################################

import asyncio


async def main():
    print('Hello from main')
    await asyncio.sleep(1)


asyncio.run(main())

#################################################################

import asyncio


async def main():
    print('Hello from main')
    await asyncio.sleep(1)


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
try:
    loop.run_until_complete(main())
finally:
    # Run the loop again to finish pending tasks
    loop.run_until_complete(asyncio.sleep(0))

    asyncio.set_event_loop(None)
    loop.close()

#################################################################

import asyncio


async def main():
    print('Hello from main')
    await asyncio.sleep(1)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
