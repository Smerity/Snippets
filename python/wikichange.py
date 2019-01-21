import json

import asyncio
import aiohttp

from aiosseclient import aiosseclient

async def main():
    async for event in aiosseclient('https://stream.wikimedia.org/v2/stream/recentchange'):
        packet = json.loads(event.data)
        if packet['wiki'] == 'enwiki' and not packet['bot']:
            out = json.dumps(packet, indent=4, sort_keys=True)
            print(out)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
