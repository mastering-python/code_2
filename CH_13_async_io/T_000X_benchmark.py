import time
import asyncio


async def slow_blocking_function(sleep):
    # Note: you should never use time.sleep() in an async function
    # Always use asyncio.sleep instead
    time.sleep(sleep)


print('Slow:')
asyncio.run(slow_blocking_function(0.5), debug=True)
print('Fast:')
asyncio.run(slow_blocking_function(0.05), debug=True)
