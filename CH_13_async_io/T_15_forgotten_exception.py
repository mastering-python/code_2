import asyncio


async def throw_exception():
    raise RuntimeError()


async def main():
    # ignoring an exception from an async def
    asyncio.create_task(throw_exception())


asyncio.run(main())
