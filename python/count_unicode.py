import sys

from collections import Counter

totals = Counter()
for line in sys.stdin:
    c = Counter(line)
    totals.update(c)

print(totals)
print(len(totals))
