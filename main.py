# version 7.3 : replaced White/Black Pawn class with Pawn, omptimized castle
# author : cheb
# chess engine

# quote of the day : "Hasta la vista, baby"

from figures import Pawn, Rook, Bishop, Knight, Queen, King, coordinates

board = [[None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]]

check = []

def look_threats(board, pieces, thr): # thr - угрозы своего цвета
    real_threats = set() # вражеские угрозы
    for piece in pieces:
        piece.move(board, thr)
        for real_threat in piece.threats:
            real_threats.add(real_threat)
    return sorted(real_threats) # возвращает вражеские угрозы


def move_piece(board, pieces, opposite_pieces, thr): 
    actual_move = input()
    threat = look_threats(board, opposite_pieces, thr) # считаем угрозы противника учитывая угрозы своего цвета
    if actual_move[0] == 'Q':
        piece_type = Queen
    elif actual_move[0] == 'N':
        piece_type = Knight
    elif actual_move[0] == 'B':
        piece_type = Bishop
    elif actual_move[0] == 'K' or actual_move[0] == 'O':
        piece_type = King
    elif actual_move[0] == 'R':
        piece_type = Rook
    else:
        piece_type = Pawn
    
    for piece in pieces:
        if not isinstance(piece, piece_type):
            continue
        if actual_move in piece.move(board, threat):
            board[piece.row][piece.col] = None
            if actual_move == 'O-O-O':
                piece.row = piece.row
                piece.col = piece.col - 2
                piece.move_count += 1
                board[piece.row][piece.col] = piece

                rook = board[piece.row][0]
                board[piece.row][0] = None
                rook.row = rook.row
                rook.col = piece.col + 1
                board[rook.row][rook.col] = rook
                return True
            elif actual_move == 'O-O':
                piece.row = piece.row
                piece.col = piece.col + 2
                piece.move_count += 1
                board[piece.row][piece.col] = piece

                rook = board[piece.row][7]
                board[piece.row][7] = None
                rook.row = rook.row
                rook.col = piece.col - 1
                board[rook.row][rook.col] = rook
                return True
            piece.row = coordinates[actual_move[-2:]][0]
            piece.col = coordinates[actual_move[-2:]][1]
            piece.move_count += 1
            board[piece.row][piece.col] = piece
            return True 
    return False

    
# white pawns
a_pawn_w = Pawn('a2', 0, board)
b_pawn_w = Pawn('b2', 0, board)
c_pawn_w = Pawn('c2', 0, board)
d_pawn_w = Pawn('d2', 0, board)
e_pawn_w = Pawn('e2', 0, board)
f_pawn_w = Pawn('f2', 0, board)
g_pawn_w = Pawn('g2', 0, board)
h_pawn_w = Pawn('h2', 0, board)


# black pawns
a_pawn_b = Pawn('a7', 1, board)
b_pawn_b = Pawn('b7', 1, board)
c_pawn_b = Pawn('c7', 1, board)
d_pawn_b = Pawn('d7', 1, board)
e_pawn_b = Pawn('e7', 1, board)
f_pawn_b = Pawn('f7', 1, board)
g_pawn_b = Pawn('g7', 1, board)
h_pawn_b = Pawn('h7', 1, board)
 
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

king_w.can_castle(board, imp_moves=[])


thr = []
b = look_threats(board, black_pieces, thr) # свои угрозы, пока не учитывая врага так как до первого хода (белые)

print(isinstance(board[7][4], King))
turn = False
while game:
    print('+---+---+---+---+---+---+---+---+')
    for line in board:
        for cell in line:
            if cell is not None:
                if cell.color == 0:
                    print(f'| \033[33m{cell.name}\033[0m', end=' ')
                else:
                    print(f'| \033[32m{cell.name}\033[0m', end=' ')
            else:
                print('|  ', end=' ')
        print('|\n+---+---+---+---+---+---+---+---+')
    print()
    if turn == False and move_piece(board, white_pieces, black_pieces, b): # учитываем угрозы врага
        turn = True
        a = look_threats(board, white_pieces, b)
    elif turn == True and move_piece(board, black_pieces, white_pieces, a):
        turn = False
        b = look_threats(board, black_pieces, a)
    else:
        print('---= Impossible move! =--- \n \t   or\n---= Incorrect input! =---')


