from decimal import Decimal

buckets = 2 ** 64
billions = 50
objects = billions * 1e9

m, n = Decimal(buckets), Decimal(objects)
expected_collisions = n - m * (1 - ((m - 1) / m) ** n)
print 'Expected total collisions with {} billion objects in a 64 bit domain: {:.2f}'.format(billions, expected_collisions)
