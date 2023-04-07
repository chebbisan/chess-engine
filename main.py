# version 10 : mozhet rabotaet
# author : cheb
# chess engine

# quote of the day : "Сломал палец на ноге...("

import sys

from figures import Pawn, Rook, Bishop, Knight, Queen, King, coordinates, get_coordinate, get_number, get_letter, Figure



board = [[None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]]


def find_duplicate_moves(moves, piece_moves, move):
    first_piece = moves[move]
    second_piece = piece_moves[move]
    if first_piece.col == second_piece.col:
        first_piece_move = move[0] + get_number(first_piece.row) + move[1:]
        second_piece_move = move[0] + get_number(second_piece.row) + move[1:]
    else:
        first_piece_move = move[0] + get_letter(first_piece.col) + move[1:]
        second_piece_move = move[0] + get_letter(second_piece.col) + move[1:]
    del moves[move]
    del piece_moves[move]
    moves[first_piece_move] = first_piece
    piece_moves[second_piece_move] = second_piece
    return True

    



def look_threats(board, pieces, thr): # thr - угрозы своего цвета
    real_threats = set() # вражеские угрозы
    for piece in pieces:
        piece.move(board, thr)
        for real_threat in piece.threats:
            real_threats.add(real_threat)
    return sorted(real_threats) # возвращает вражеские угрозы


            
def safe_move(board, pieces, thr):
    moves = {}
    moves_ = dict(moves)
    for piece in pieces:
        piece_moves = piece.move(board, thr)
        for move in moves_:
            if move in piece_moves and moves_[move] is not piece:
                # print(move, piece.col, moves[move].col)
                find_duplicate_moves(moves, piece_moves, move)
                # print(moves, '\n' ,piece_moves)
        moves = moves | piece_moves
        moves_ = moves | piece_moves
        if piece.move_count != 0:
            piece.move_count += 1 
    for move in moves_:
        if move == 'O-O-O' or move == 'O-O':
            continue
        piece = moves[move]
        if '=' in move:
            new_row, new_col = coordinates[move[:2]][0], coordinates[move[:2]][1]
            promote_to = move[-1]
            return_piece = piece
            pieces.remove(piece)
            if promote_to == 'Q':
                piece = Queen(move[:2], piece.color, board)
            elif promote_to == 'R':
                piece = Rook(move[:2], piece.color, board)
            elif promote_to == 'B':
                piece = Bishop(move[:2], piece.color, board)
            elif promote_to == 'N':
                piece = Knight(move[:2], piece.color, board)
            pieces.append(piece)
            old_row, old_col = return_piece.row, return_piece.col
            cell = None
        else:
            new_row, new_col = coordinates[move[-2:]][0], coordinates[move[-2:]][1]
            old_row, old_col = piece.row, piece.col
            cell = board[new_row][new_col] ####
        board[old_row][old_col] = None
        piece.row = new_row
        piece.col = new_col

        board[new_row][new_col] = piece

        if piece.color == 0:
            if isinstance(cell, Figure):
                black_pieces.remove(cell)
                thre = look_threats(board, black_pieces, thr)
                black_pieces.append(cell)
            else:
                thre = look_threats(board, black_pieces, thr)
            if king_w.under_check(thre):
                del moves[move]
            piece.row = old_row
            piece.col = old_col
            board[new_row][new_col] = cell
            board[old_row][old_col] = piece

        elif piece.color == 1:
            if isinstance(cell, Figure):
                white_pieces.remove(cell)
                thre = look_threats(board, white_pieces, thr)
                white_pieces.append(cell)
            else:
                thre = look_threats(board, white_pieces, thr)
            if king_b.under_check(thre):
                del moves[move]
            piece.row = old_row
            piece.col = old_col
            board[new_row][new_col] = cell
            board[old_row][old_col] = piece
        if '=' in move:
            pieces.remove(piece)
            del piece
            pieces.append(return_piece)
            return_piece.row = old_row
            return_piece.col = old_col
            board[new_row][new_col] = cell
            board[old_row][old_col] = return_piece
    return moves



def move_piece(board, pieces, thr):
    
    # threat = look_threats(board, opposite_pieces, thr) # считаем угрозы противника учитывая угрозы своего цвета
    # if actual_move[0] == 'Q':
    #     piece_type = Queen
    # elif actual_move[0] == 'N':
    #     piece_type = Knight
    # elif actual_move[0] == 'B':
    #     piece_type = Bishop
    # elif actual_move[0] == 'K' or actual_move[0] == 'O':
    #     piece_type = King
    # elif actual_move[0] == 'R':
    #     piece_type = Rook
    # else:
    #     piece_type = Pawn

    # print(thr)
    moves = safe_move(board, pieces, thr)
    print(moves)
    if moves:
        actual_move = input()
                
        if actual_move in moves:
            piece = moves[actual_move]
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
            
            old_row = piece.row
            if '=' in actual_move:
                new_row, new_col = coordinates[actual_move[:2]][0], coordinates[actual_move[:2]][1]
                promote_to = actual_move[-1]
                pieces.remove(piece)
                if promote_to == 'Q':
                    piece = Queen(actual_move[:2], piece.color, board)
                elif promote_to == 'R':
                    piece = Rook(actual_move[:2], piece.color, board)
                elif promote_to == 'B':
                    piece = Bishop(actual_move[:2], piece.color, board)
                elif promote_to == 'N':
                    piece = Knight(actual_move[:2], piece.color, board)
                pieces.append(piece)
            else:
                new_row, new_col = coordinates[actual_move[-2:]][0], coordinates[actual_move[-2:]][1]

            if 'x' in actual_move:
                if board[new_row][new_col] is None:
                    pieces.remove(board[old_row][new_col])
                    board[old_row][new_col] = None
                else:
                    pieces.remove(board[new_row][new_col])


            
            piece.row = new_row
            piece.col = new_col
            board[new_row][new_col] = piece
            piece.move_count += 1

            return True 
        return False
    else:
        print('Mate/Stalemate!')
        sys.exit()
        

    
# # white pawns
# a_pawn_w = Pawn('a2', 0, board)
# b_pawn_w = Pawn('b2', 0, board)
# c_pawn_w = Pawn('c2', 0, board)
# d_pawn_w = Pawn('d2', 0, board)
e_pawn_w = Pawn('e7', 0, board)
# f_pawn_w = Pawn('f2', 0, board)
# g_pawn_w = Pawn('g2', 0, board)
# h_pawn_w = Pawn('h2', 0, board)


# # black pawns
# a_pawn_b = Pawn('a7', 1, board)
# b_pawn_b = Pawn('b7', 1, board)
# c_pawn_b = Pawn('c7', 1, board)
# d_pawn_b = Pawn('d7', 1, board)
# e_pawn_b = Pawn('e7', 1, board)
# f_pawn_b = Pawn('f7', 1, board)
# g_pawn_b = Pawn('g7', 1, board)
# h_pawn_b = Pawn('h7', 1, board)
 
# # white knights
# b_knight_w = Knight('b1', 0, board)
# g_knight_w = Knight('g1', 0, board)

# # black knights
# b_knight_b = Knight('b8', 1, board)
# g_knight_b = Knight('g8', 1, board)

# # white bishops 
# c_bishop_w = Bishop('c1', 0, board)
# f_bishop_w = Bishop('f1', 0, board)

# # black bishops
# c_bishop_b = Bishop('c8', 1, board)
# f_bishop_b = Bishop('f8', 1, board)

# # # white rooks
# a_rook_w = Rook('a1', 0, board)
# h_rook_w = Rook('h1', 0, board)

# # black rooks
# a_rook_b = Rook('a8', 1, board)
# h_rook_b = Rook('h8', 1, board)

# # white queen
# queen_w = Queen('d1', 0, board)

# # black queen 
# queen_b = Queen('d8', 1, board)

# white king
king_w = King('h1', 0, board)

# black king 
king_b = King('h8', 1, board)


white_pieces = []
black_pieces = []

for line in board:
    for cell in line:
        if cell is not None:
            if cell.color == 0:
                white_pieces.append(cell)
            else:
                black_pieces.append(cell)




cnt = 0
game = True

b = look_threats(board, black_pieces, thr=[]) # угроза черных на 1 ход

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
    if turn == False and move_piece(board, white_pieces, b): # учитываем угрозы врага
        turn = True
        a = look_threats(board, white_pieces, b)
    elif turn == True and move_piece(board, black_pieces, a):
        turn = False
        b = look_threats(board, black_pieces, a)
    else:
        print('---= Impossible move! =--- \n \t   or\n---= Incorrect input! =---')


