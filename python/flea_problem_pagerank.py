'''
From Connie Yang's father:
On a standard chessboard, there is a flea in every square. Every second, all the fleas jump! They can jump only to adjacent squares (no diagonals). Over time, this stabilizes. What's the expected value of empty cells?
'''

import numpy as np
import matplotlib.pyplot as plt

# Chess board is 8x8
# Each board contains one flea
prev = np.ones((8, 8), dtype=np.float)
board = np.ones((8, 8), dtype=np.float)

def get_valid_moves(i, j):
    moves = [(i + dx, j + dy) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))]
    moves = [(x, y) for x, y in moves if (0 <= x < 8 and 0 <= y < 8)]
    return moves

def print_board(board):
    # Inspect the flea board
    for i in xrange(8):
        for j in xrange(8):
            print '{:2.2f}'.format(board[i, j]),
        print

LOOPS = 50
for loop in xrange(LOOPS):
    # Ensure we don't lose any fleas
    assert(63.5 <= board.sum() <= 64.5)
    ###
    if loop % 10 == 0:
        print 'Iteration {}'.format(loop)
        print_board(board)
        print '---'
    ###
    prev, board = board, prev
    board *= 0
    for i in xrange(8):
        for j in xrange(8):
            moves = get_valid_moves(i, j)
            mass = prev[i, j] / float(len(moves))
            for pos in moves:
                board[pos] += mass

print_board(board)

mb = np.zeros((8, 8))
plt.imshow(board, interpolation='none', cmap=plt.get_cmap('OrRd'))
plt.colorbar()
plt.show()
