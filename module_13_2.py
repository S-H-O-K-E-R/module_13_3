import asyncio

async def f (no1, no2):
    print(f"{no1+no2}")
    for i in range(1, no2):
        await asyncio.sleep(i - no2)
    print

async def setup():
    task_1 = asyncio.create_task(f(1, 3))
    task_2 = asyncio.create_task(f(1, 4))
    task_3 = asyncio.create_task(f(1, 5))
    await task_1
    await task_2
    await task_3

asyncio.run(setup())