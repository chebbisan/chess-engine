# version 4 : fixed rook issue, optimized get_coordinate()
# author : cheb
# chess engine

# small fixes

from pawn import WhitePawn, BlackPawn, Rook, Bishop

board = [[0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]

# coordinates = {
#     'a8': (0, 0), 'b8': (0, 1), 'c8': (0, 2), 'd8': (0, 3), 'e8': (0, 4), 'f8': (0, 5), 'g8': (0, 6), 'h8': (0, 7),
#     'a7': (1, 0), 'b7': (1, 1), 'c7': (1, 2), 'd7': (1, 3), 'e7': (1, 4), 'f7': (1, 5), 'g7': (1, 6), 'h7': (1, 7),
#     'a6': (2, 0), 'b6': (2, 1), 'c6': (2, 2), 'd6': (2, 3), 'e6': (2, 4), 'f6': (2, 5), 'g6': (2, 6), 'h6': (2, 7),
#     'a5': (3, 0), 'b5': (3, 1), 'c5': (3, 2), 'd5': (3, 3), 'e5': (3, 4), 'f5': (3, 5), 'g5': (3, 6), 'h5': (3, 7),
#     'a4': (4, 0), 'b4': (4, 1), 'c4': (4, 2), 'd4': (4, 3), 'e4': (4, 4), 'f4': (4, 5), 'g4': (4, 6), 'h4': (4, 7),
#     'a3': (5, 0), 'b3': (5, 1), 'c3': (5, 2), 'd3': (5, 3), 'e3': (5, 4), 'f3': (5, 5), 'g3': (5, 6), 'h3': (5, 7),
#     'a2': (6, 0), 'b2': (6, 1), 'c2': (6, 2), 'd2': (6, 3), 'e2': (6, 4), 'f2': (6, 5), 'g2': (6, 6), 'h2': (6, 7),
#     'a1': (7, 0), 'b1': (7, 1), 'c1': (7, 2), 'd1': (7, 3), 'e1': (7, 4), 'f1': (7, 5), 'g1': (7, 6), 'h1': (7, 7)}

    
# white pawns
a_pawn_w = WhitePawn('a2', board)

b_pawn_w = WhitePawn('b2', board)

c_pawn_w = WhitePawn('c2', board)

d_pawn_w = WhitePawn('d2', board)

e_pawn_w = WhitePawn('e2', board)

f_pawn_w = WhitePawn('f2', board)

g_pawn_w = WhitePawn('g2', board)

h_pawn_w = WhitePawn('h2', board)


# black pawns
a_pawn_b = BlackPawn('a7', board)

b_pawn_b = BlackPawn('b7', board)

c_pawn_b = BlackPawn('c7', board)

d_pawn_b = BlackPawn('d7', board)

e_pawn_b = BlackPawn('e7', board)

f_pawn_b = BlackPawn('f7', board)

g_pawn_b = BlackPawn('g7', board)

h_pawn_b = BlackPawn('h7', board)


a_rook_w = Rook('e5', 1, board)

print(a_rook_w.move(board))

for line in board:
    print(line)
