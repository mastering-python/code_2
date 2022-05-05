import asyncio


async def sub_printer():
    print('Hi from the sub-printer')


async def printer():
    print('Before creating the sub-printer task')
    asyncio.create_task(sub_printer())
    print('After creating the sub-printer task')


async def main():
    asyncio.create_task(printer())
    await asyncio.sleep(0.1)

asyncio.run(main())
