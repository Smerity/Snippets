from __future__ import division
import math

# Number of bits (first term is total MB)
n = 512 * 1024 ** 3
# Number of hash functions
k = 4
# Total number of elements
m = 100e9

print '{:.0f} objects into an\n{} bit array with\n{} hash functions'.format(m, n, k)

exponent = (k * m) / n
fp = (1 - math.e ** (-exponent)) ** k

print 'Probability of false positive: {}'.format(fp)
