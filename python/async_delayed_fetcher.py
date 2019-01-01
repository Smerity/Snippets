import time

import asyncio

from asyncio import Queue

from contextlib import suppress

class CrawlDelayException(Exception):
    def __init__(self, message, delay=None):
        super().__init__(message)
        self.delay = delay

class Server(object):
    def __init__(self, delay=None):
        self.delay = delay
        self.requests = [0]

    def get(self, k):
        self.requests.append(time.time())
        assert self.requests[-2] - self.requests[-1] > self.delay
        return 42

class Domain(object):
    def __init__(self, domain):
        self.domain = domain
        self.requests = Queue()

        loop = asyncio.get_event_loop()
        self.fetcher = loop.create_task(self.fetch_loop())

    async def fetch_loop(self):
        print('Domain({}): Fetch loop started'.format(self.domain))
        while True:
            addr, future = await self.requests.get()
            # Start an asynchronous sleep of crawl delay in length
            print('Domain({}): Fetching {}'.format(self.domain, addr))
            await asyncio.sleep(1)
            # Wait until the async sleep with crawl delay is complete
            future.set_result(42)

    async def get(self, addr):
        future = loop.create_future()
        await self.requests.put((addr, future))
        print('Q:', self.requests.qsize())
        print('Domain({}): Queued {}'.format(self.domain, addr))
        return future

    async def close(self):
        # Cancelling only starts the process to cancel
        self.fetcher.cancel()
        # We must wait for the task itself to complete
        await self.fetcher

async def fetch_pages(d):
    # Must await the get request to get the Futures
    requests = [await d.get(addr) for addr in ['r/ML', 'r/news', 'r/aww']]
    # Must await the response of the Futures to get the data
    await asyncio.gather(*requests)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    d = Domain('reddit.com')

    # Get all fetch requests simultaneously
    loop.run_until_complete(fetch_pages(d))

    # https://stackoverflow.com/questions/47514100/thread-and-asyncio-task-was-destroyed-but-it-is-pending
    with suppress(asyncio.CancelledError):
        loop.run_until_complete(d.close())

    loop.close()

    print('Done')
