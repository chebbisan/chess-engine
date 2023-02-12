# version 4 : added bishop
# author : cheb
# chess engine

# need to optimize bishop

from pawn import WhitePawn, BlackPawn, Rook, Bishop

board = [[0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]

coordinates = {
    'a8': (0, 0), 'b8': (0, 1), 'c8': (0, 2), 'd8': (0, 3), 'e8': (0, 4), 'f8': (0, 5), 'g8': (0, 6), 'h8': (0, 7),
    'a7': (1, 0), 'b7': (1, 1), 'c7': (1, 2), 'd7': (1, 3), 'e7': (1, 4), 'f7': (1, 5), 'g7': (1, 6), 'h7': (1, 7),
    'a6': (2, 0), 'b6': (2, 1), 'c6': (2, 2), 'd6': (2, 3), 'e6': (2, 4), 'f6': (2, 5), 'g6': (2, 6), 'h6': (2, 7),
    'a5': (3, 0), 'b5': (3, 1), 'c5': (3, 2), 'd5': (3, 3), 'e5': (3, 4), 'f5': (3, 5), 'g5': (3, 6), 'h5': (3, 7),
    'a4': (4, 0), 'b4': (4, 1), 'c4': (4, 2), 'd4': (4, 3), 'e4': (4, 4), 'f4': (4, 5), 'g4': (4, 6), 'h4': (4, 7),
    'a3': (5, 0), 'b3': (5, 1), 'c3': (5, 2), 'd3': (5, 3), 'e3': (5, 4), 'f3': (5, 5), 'g3': (5, 6), 'h3': (5, 7),
    'a2': (6, 0), 'b2': (6, 1), 'c2': (6, 2), 'd2': (6, 3), 'e2': (6, 4), 'f2': (6, 5), 'g2': (6, 6), 'h2': (6, 7),
    'a1': (7, 0), 'b1': (7, 1), 'c1': (7, 2), 'd1': (7, 3), 'e1': (7, 4), 'f1': (7, 5), 'g1': (7, 6), 'h1': (7, 7)}

    
# white pawns
a_pawn_w = WhitePawn('a2')
board[coordinates['a2'][0]][coordinates['a2'][1]] = a_pawn_w.color

b_pawn_w = WhitePawn('b2')
board[coordinates['b2'][0]][coordinates['b2'][1]] = b_pawn_w.color

c_pawn_w = WhitePawn('c2')
board[coordinates['c2'][0]][coordinates['c2'][1]] = c_pawn_w.color

d_pawn_w = WhitePawn('d2')
board[coordinates['d2'][0]][coordinates['d2'][1]] = d_pawn_w.color

e_pawn_w = WhitePawn('e2')
board[coordinates['e2'][0]][coordinates['e2'][1]] = e_pawn_w.color

f_pawn_w = WhitePawn('f2')
board[coordinates['f2'][0]][coordinates['f2'][1]] = f_pawn_w.color

g_pawn_w = WhitePawn('g2')
board[coordinates['g2'][0]][coordinates['g2'][1]] = g_pawn_w.color

h_pawn_w = WhitePawn('h2')
board[coordinates['h2'][0]][coordinates['h2'][1]] = h_pawn_w.color


# black pawns
a_pawn_b = BlackPawn('a7')
board[coordinates['a7'][0]][coordinates['a7'][1]] = a_pawn_b.color

b_pawn_b = BlackPawn('b7')
board[coordinates['b7'][0]][coordinates['b7'][1]] = b_pawn_b.color

c_pawn_b = BlackPawn('c7')
board[coordinates['c7'][0]][coordinates['c7'][1]] = c_pawn_b.color

d_pawn_b = BlackPawn('d7')
board[coordinates['d7'][0]][coordinates['d7'][1]] = d_pawn_b.color

e_pawn_b = BlackPawn('e7')
board[coordinates['e7'][0]][coordinates['e7'][1]] = e_pawn_b.color

f_pawn_b = BlackPawn('f7')
board[coordinates['f7'][0]][coordinates['f7'][1]] = f_pawn_b.color

g_pawn_b = BlackPawn('g7')
board[coordinates['g7'][0]][coordinates['g7'][1]] = g_pawn_b.color

h_pawn_b = BlackPawn('h7')
board[coordinates['h7'][0]][coordinates['h7'][1]] = h_pawn_b.color


a_rook_w = Rook('e5', 1)
board[coordinates['e5'][0]][coordinates['e5'][1]] = 5 * a_rook_w.color

bishop_w = Bishop('d5', 1)
board[coordinates['d5'][0]][coordinates['d5'][1]] = 3 * bishop_w.color

print(a_rook_w.move(board))
print(bishop_w.move(board))

for line in board:
    print(line)
