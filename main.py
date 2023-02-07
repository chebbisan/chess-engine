# version 0.01 : board and pawn move
# author : cheb
# chess engine

from pawn import Pawn

board = [[0, 0, 0, 0, 0, 0, 0, 0]] * 8

king_pawn = Pawn(5, 3)
king_pawn.move()
