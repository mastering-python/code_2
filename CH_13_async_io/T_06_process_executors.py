import time
import asyncio
import concurrent.futures


def executor_sleep():
    print('before sleep')
    time.sleep(1)
    print('after sleep')


async def executor_sleeps(n):
    loop = asyncio.get_running_loop()
    futures = []
    with concurrent.futures.ProcessPoolExecutor() as pool:
        for _ in range(n):
            future = loop.run_in_executor(pool, executor_sleep)
            futures.append(future)

        await asyncio.gather(*futures)


if __name__ == '__main__':
    start = time.time()
    asyncio.run(executor_sleeps(2))
    print(f'duration: {time.time() - start:.0f}')
