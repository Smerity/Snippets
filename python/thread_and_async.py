import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

# Partially inspired by https://stackoverflow.com/questions/28492103/how-to-combine-python-asyncio-with-threads

# An async beeper fills a queue that is then consumed by a normal thread

def cpu_bound_operation(x, results):
    time.sleep(x)
    total = 0
    print('meow', results)

    print('emptying results ...')
    while results:
        total += results.pop()
    print('emptied - total of', total)

    time.sleep(x)
    print('woof', results)

    print('emptying results ...')
    while results:
        total += results.pop()
    print('emptied - total of', total)

# Infinite loop
async def beep(results):
    i = 0
    while True:
        print('- beep of', i)
        results.append(i)
        i += 1
        await asyncio.sleep(1)

@asyncio.coroutine
def main(results):
    # cpu_bound_operation goes in ThreadPoolExecutor
    # This avoids blocking the loop
    yield from loop.run_in_executor(p, cpu_bound_operation, *[3, results])


loop = asyncio.get_event_loop()
results = []
p = ThreadPoolExecutor(2)
asyncio.run_coroutine_threadsafe(beep(results), loop)
loop.run_until_complete(main(results))
