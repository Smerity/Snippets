from math import fsum
#Return an accurate floating point sum of values in the iterable.
#Assumes IEEE-754 floating point arithmetic.

print '0.1 x 10 using sum: %r' % sum(0.1 for x in xrange(10))
print '0.1 x 10 using fsum: %r' % fsum(0.1 for x in xrange(10))
