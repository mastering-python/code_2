import time
import asyncio


async def main():
    # Oh no... a synchronous sleep from asyncio code
    time.sleep(0.2)


asyncio.run(main(), debug=True)
