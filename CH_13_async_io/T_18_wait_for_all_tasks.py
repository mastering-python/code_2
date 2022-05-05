import asyncio


async def sub_printer():
    print('Hi from the sub-printer')


async def printer():
    print('Before creating the sub-printer task')
    asyncio.create_task(sub_printer())
    print('After creating the sub-printer task')


async def main():
    asyncio.create_task(printer())
    await shutdown()


async def shutdown(timeout=5):
    tasks = []
    # Collect all tasks from `asyncio`
    for task in asyncio.all_tasks():
        # Make sure we skip our current task so we don't loop
        if task is not asyncio.current_task():
            tasks.append(task)

    for future in asyncio.as_completed(tasks, timeout=timeout):
        await future

asyncio.run(main())
