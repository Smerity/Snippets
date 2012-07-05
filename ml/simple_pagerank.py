import random

class Node(object):
    __slots__ = ["name", "edges", "pagerank", "partial"]
    def __init__(self, edges=None):
        # The edges out from this node
        self.edges = edges or set()
        self.partial = 0
        self.pagerank = 0
    def __str__(self):
        return "[%d edges -- PR %2.3f]" % (len(self.edges), self.pagerank)
    def __repr__(self):
        return self.__str__()

def create_graph():
    total = 100
    nodes = [Node() for i in xrange(total)]
    # Set initial PageRank -- all evenly distributed
    for n in nodes:
        n.pagerank = 1/float(total)
    for i in xrange(4*total):
        dest = random.choice(nodes)
        src = random.choice(nodes)
        src.edges.add(dest)
    return nodes

def pagerank_iteration(nodes, alpha=0.1):
    # P(n) = \alpha * (1/|G|) + (1-\alpha) \sum P(m)/C(m)

    # Accumulate dangling mass for the final step
    dangling_mass = 0
    # Scratchpad for partial PageRank computation
    for n in nodes:
        n.partial = 0
    # Each node distributes it's PageRank mass along the outgoing links
    # Map step
    for n in nodes:
        for e in n.edges:
            e.partial += n.pagerank/float(len(n.edges))
        else:
            dangling_mass += n.pagerank
    # Calculate final PageRank including dangling nodes and teleportation factor
    # Reduce step
    for n in nodes:
        n.pagerank = alpha * (1/float(len(nodes)))
        n.pagerank += (1-alpha) * ((dangling_mass/float(len(nodes))) + n.partial)
    # Renormalise the distribution
    # Reduce step
    total_mass = float(sum(n.pagerank for n in nodes))
    for n in nodes:
        n.pagerank /= total_mass

from pprint import pprint
nodes = create_graph()
pprint(nodes)
print
for i in xrange(10):
    pagerank_iteration(nodes)
    pprint(nodes)
    print

print "Final Tally (with incoming link counts)"
print "=-=-=" * 8
for n in nodes:
    print "%s with %d incoming links" % (n, sum(n in m.edges for m in nodes))
