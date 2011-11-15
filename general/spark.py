#!/usr/bin/python
# -*- coding: UTF-8 -*-
# See http://news.ycombinator.com/item?id=3237478
# and https://github.com/holman/spark/wiki/Wicked-Cool-Usage
# and https://github.com/bitly/data_hacks

BARS = u'▁▂▃▅▆▇'

import sys

if sys.argv[1:]:
    data = sys.argv[1:]
else:
    data = sys.stdin

data = (x.strip() for x in data)
data = [float(x) for x in data if x]
m = min(data)
w = max(data) / len(BARS)

bins = [((i-1)*w+m+w, i*w+m+w)
         for i in range(len(BARS))]

indexes = [i for n in data
           for (i, (lo, hi)) in enumerate(bins)
           if lo <= n < hi]

print ''.join(BARS[i] for i in indexes)
