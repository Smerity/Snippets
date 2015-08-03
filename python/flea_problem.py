'''
From Connie Yang's father:
On a standard chessboard, there is a flea in every square. Every second, all the fleas jump! They can jump only to adjacent squares (no diagonals). Over time, this stabilizes. What's the expected value of empty cells?
'''

import random
import numpy as np
import matplotlib.pyplot as plt

# Chess board is 8x8
# Each board contains one flea
prev = np.ones((8, 8), dtype=np.int)
board = np.ones((8, 8), dtype=np.int)
heatmap = np.zeros((8, 8), dtype=np.int)

def get_valid_moves(i, j):
    moves = [(i + dx, j + dy) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))]
    moves = [(x, y) for x, y in moves if (0 <= x < 8 and 0 <= y < 8)]
    return moves

def print_board(board):
    # Inspect the flea board
    for i in xrange(8):
        for j in xrange(8):
            print board[i, j],
        print

empty = []
LOOPS = 10000
for loop in xrange(LOOPS):
    # Ensure we don't lose any fleas
    assert(board.sum() == 8 * 8)
    empty.append(sum(1 for i in xrange(8) for j in xrange(8) if board[i, j] == 0))
    ###
    # Add current state to the heatmap
    for i in xrange(8):
        for j in xrange(8):
            heatmap[i, j] += board[i, j]
    if loop % 1000 == 0:
        print 'Iteration {}'.format(loop)
        print 'Total empty: {}'.format(empty[-1])
        print_board(board)
        print '---'
    ###
    prev, board = board, prev
    board *= 0
    for i in xrange(8):
        for j in xrange(8):
            for flea in xrange(prev[i, j]):
                pos = random.choice(get_valid_moves(i, j))
                board[pos] += 1

print_board(heatmap)

print 'Average empty over {} iterations: {}'.format(LOOPS, sum(empty) / float(len(empty)))

x = range(0, LOOPS)
fig = plt.figure(figsize=(12, 4.5))
plt.xlim((0, LOOPS))
plt.ylim((0, 64))
plt.fill_between(x, empty, 0, alpha=0.45)
plt.ylabel('Empty cells (pct)')
plt.xlabel('Iteration')
fig.savefig('fleas.png')
plt.show(block=True)

'''
Saved heatmap from 100k (for probabilities):
57357 86250 86041 85930 85917 86443 86818 57535
86323 115285 114742 114333 114393 115101 115574 85914
86105 114935 114798 114989 114595 114902 114762 85560
85557 114305 114367 114538 114891 115167 114144 85402
85311 113788 113832 114067 114698 115072 114708 85868
85307 113509 113037 113879 114311 114095 114390 85413
84917 113107 113190 113599 113671 113301 114029 85059
56507 85133 85447 85363 85243 85027 85362 56787
'''

mb = np.zeros((8, 8))
plt.imshow(heatmap, interpolation='none', cmap=plt.get_cmap('OrRd'))
plt.colorbar()
plt.show()
