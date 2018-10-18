import asyncio
import random
import types

async def slow_task():
    await asyncio.sleep(random.uniform(0.1, 5))
    return random.choice('abcdefghijklmnop')

async def get_batches(batch_size, total):
    tasks = [slow_task() for i in range(total)]
    result = []

    finished, unfinished = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    while unfinished:
        result += [task.result() for task in finished]
        # Yield if we have a full batch to give
        while len(result) > batch_size:
            yield result[:batch_size]
            result = result[batch_size:]
        finished, unfinished = await asyncio.wait(unfinished, return_when=asyncio.FIRST_COMPLETED)
    result += [task.result() for task in finished]
    # Keep yielding the result until we're complete
    while result:
        yield result[:batch_size]
        result = result[batch_size:]

async def print_batches():
    async for result in get_batches(batch_size=4, total=42):
        print(result)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    loop.run_until_complete(print_batches())

    loop.close()
