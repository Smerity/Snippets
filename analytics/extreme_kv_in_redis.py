#! /usr/bin/env python
## Storing hundreds of millions of simple key-value pairs in Redis
# See: http://news.ycombinator.com/item?id=3183276
# See: http://instagram-engineering.tumblr.com/post/12202313862/storing-hundreds-of-millions-of-simple-key-value-pairs

import redis
import random
import pylibmc
import sys

r = redis.Redis(host = 'localhost', port = 6389)
mc = pylibmc.Client(['localhost:11222'])

REDIS_SETGET = False
REDIS_HSET = False
MC = False

NUM_ENTRIES = 1000000
MAX_VAL = 12000000

if len(sys.argv) != 2 or sys.argv[1] not in ('redis-normal', 'redis-hashes', 'memcached'):
    print 'Specify a test: redis-normal, redis-hashes, memcached'
    print 'NOTE: clear out memcached (restart) or Redis (FLUSHALL) before running'
    sys.exit(2)
if sys.argv[1] == 'redis-normal':
    REDIS_SETGET = True
elif sys.argv[1] == 'redis-hashes':
    REDIS_HSET = True
elif sys.argv[1] == 'memcached':
    MC = True

p = r.pipeline()
for i in xrange(0, NUM_ENTRIES):
    value = random.randint(0, MAX_VAL)
    if MC:
        mc.set(str(i), value)
    elif REDIS_SETGET:
        r.set(str(i), value)
    elif REDIS_HSET:
        bucket = int(i / 500)
        p.hset(bucket, i, value)

    if i % (NUM_ENTRIES/10) == 0:
        if REDIS_SETGET or REDIS_HSET:
            p.execute()
            p = r.pipeline()
        print i

# one final clear out
if REDIS_SETGET or REDIS_HSET:
    p.execute()

# get size
if MC:
    size = int(mc.get_stats()[0][1]['bytes'])
elif (REDIS_SETGET or REDIS_HSET):
    size = int(r.info()['used_memory'])

print '%s bytes, %s MB' % (size, size / 1024 / 1024)
