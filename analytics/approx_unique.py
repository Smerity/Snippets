# Approximate unique count using the same techniques as Google's SZL
# Given N objects, hash each object and store the lowest M (s.t. M << N) hashes
# Assuming uniform distribution, ...
# 1) calculate what percentage of hash space is covered
# 2) compare this to how much of the hash space would be expected to be covered
# http://code.google.com/p/szl/source/browse/trunk/src/emitters/szlunique.cc
# (found via http://news.ycombinator.com/item?id=3803524)

## Wall Street Journal -- Section 00
# 7884 words in the exact unique count
# 6125 words in the estimated unique count

## Wall Street Journal -- Section 00-23
# 46581 words in the exact unique count
# 42923 words in the estimated unique count
#--- cat ~/Corpora/gold/wsj00.raw ~/Corpora/gold/wsj02-21.raw ~/Corpora/gold/wsj23.raw | sed 's/ /\n/g' | time python -m cProfile approx_unique.py

import hashlib

def _add_element(nsmallest, nset, h):
  nsmallest.append(h)
  nset.add(h)
  nsmallest.sort()

def check_element(x, nsmallest, nset, nsize):
  # TODO: Use a more efficient data structure than Python list for nsmallest
  h = hashlib.md5(x).hexdigest()
  if not nsmallest or (h not in nset and h < nsmallest[-1]):
    # If more hashes than allocated, remove the largest hash
    if len(nsmallest) >= nsize:
      val = nsmallest.pop()
      nset.remove(val)
    _add_element(nsmallest, nset, h)

def predict_unique(nsmallest):
  # MD5 hash range: 128 bits
  hash_range = 2**128
  portion = int(nsmallest[-1], 16)
  # Number of portion slices that would fit in the hash range
  nportions = hash_range / float(portion)
  # Predicted unique objects = number of portions * size of a portion
  return nportions * len(nsmallest)

if __name__ == "__main__":
  import sys
  words = [x.rstrip() for x in sys.stdin.readlines()]
  print "%d in the exact unique count" % len(set(words))
  nsm = []
  nset = set()
  [check_element(x, nsm, nset, 100) for x in words]
  print "%d in the estimated unique count" % predict_unique(nsm)
