# version 7.1 : second castle variation (completed) (playable)
# author : cheb
# chess engine

# quote of the day : "Access granted"

from figures import WhitePawn, BlackPawn, Rook, Bishop, Knight, Queen, King, coordinates

board = [[None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]]

check = []

def look_threats(board, pieces, thr, rooks): # thr - угрозы своего цвета
    real_threats = set() # вражеские угрозы
    for piece in pieces:
        piece.move(board, thr, rooks)
        for real_threat in piece.threats:
            real_threats.add(real_threat)
    return sorted(real_threats) # возвращает вражеские угрозы


def move_piece(board, pieces, opposite_pieces, thr, rooks): 
    actual_move = input()
    threat = look_threats(board, opposite_pieces, thr, rooks) # считаем угрозы противника учитывая угрозы своего цвета

    for piece in pieces:
        if actual_move in piece.move(board, threat, rooks):
            board[piece.row][piece.col] = None
            if actual_move == 'O-O-O':
                piece.row = piece.row
                piece.col = piece.col - 2
                board[piece.row][piece.col] = piece
                
                board[rooks[0 + piece.color].row][rooks[0 + piece.color].col] = None
                rooks[0 + piece.color].row = rooks[0 + piece.color].row
                rooks[0 + piece.color].col = piece.col + 1
                board[rooks[0 + piece.color].row][rooks[0 + piece.color].col] = rooks[0 + piece.color]
                return True
            elif actual_move == 'O-O':
                piece.row = piece.row
                piece.col = piece.col + 2
                board[piece.row][piece.col] = piece

                board[rooks[2 + piece.color].row][rooks[2 + piece.color].col] = None
                rooks[2 + piece.color].row = rooks[2 + piece.color].row
                rooks[2 + piece.color].col = piece.col - 1
                board[rooks[2 + piece.color].row][rooks[2 + piece.color].col] = rooks[2 + piece.color]
                return True
            piece.row = coordinates[actual_move[-2:]][0]
            piece.col = coordinates[actual_move[-2:]][1]
            board[piece.row][piece.col] = piece
            return True 
    return False

    
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

# white knights
b_knight_w = Knight('b1', 0, board)
g_knight_w = Knight('g1', 0, board)

# black knights
b_knight_b = Knight('b8', 1, board)
g_knight_b = Knight('g8', 1, board)

# white bishops 
c_bishop_w = Bishop('c1', 0, board)
f_bishop_w = Bishop('f1', 0, board)

# black bishops
c_bishop_b = Bishop('c8', 1, board)
f_bishop_b = Bishop('f8', 1, board)

# white rooks
a_rook_w = Rook('a1', 0, board)
h_rook_w = Rook('h1', 0, board)

# black rooks
a_rook_b = Rook('a8', 1, board)
h_rook_b = Rook('h8', 1, board)

# white queen
queen_w = Queen('d1', 0, board)

# black queen 
queen_b = Queen('d8', 1, board)

# white king
king_w = King('e1', 0, board)

# black king 
king_b = King('e8', 1, board)

white_pieces = [a_pawn_w, b_pawn_w, c_pawn_w, d_pawn_w, e_pawn_w, f_pawn_w, g_pawn_w, h_pawn_w, b_knight_w, g_knight_w, c_bishop_w, f_bishop_w,
    a_rook_w, h_rook_w, queen_w, king_w]

black_pieces = [a_pawn_b, b_pawn_b, c_pawn_b, d_pawn_b, e_pawn_b, f_pawn_b, g_pawn_b, h_pawn_b, b_knight_b, g_knight_b, c_bishop_b, f_bishop_b,
    a_rook_b, h_rook_b, queen_b, king_b]


cnt = 0
game = True

rooks = [a_rook_w, a_rook_b, h_rook_w, h_rook_b]
king_w.can_castle(board, rooks, imp_moves=[])


table = open(r'chess_table.txt')
for line in table:
    print(line, end='')
table.close()
thr = []
b = look_threats(board, black_pieces, thr, rooks) # свои угрозы, пока не учитывая врага так как до первого хода (белые)

turn = 0
while game:
    for line in board:
        print(line)
    print()
    if turn == 0 and move_piece(board, white_pieces, black_pieces, b, rooks): # учитываем угрозы врага
        turn = 1
        a = look_threats(board, white_pieces, b, rooks)
    elif turn == 1 and move_piece(board, black_pieces, white_pieces, a, rooks):
        turn = 0
        b = look_threats(board, black_pieces, a, rooks)
    else:
        print('---= Impossible move! =--- \n \t   or\n---= Incorrect input! =---')


