# version 10 : mozhet rabotaet
# author : cheb
# chess engine

# quote of the day : "Сломал палец на ноге...("

import sys
import enum

from figures import Pawn, Rook, Bishop, Knight, Queen, King, coordinates, get_coordinate, get_number, get_letter, Figure


class Color(enum.IntEnum):
    WHITE = 0
    BLACK = 1


def opposing_color(color: Color) -> Color:
    return Color.BLACK if color == Color.WHITE else Color.WHITE

def MakeMove(move, moves, current_turn):
    piece = moves[move]
    print_board(board)
    board[piece.row][piece.col] = None
    
    cell = None
    
    if move == 'O-O-O':
        new_row, new_col = piece.row, piece.col - 2
        rook = board[piece.row][0]
        board[rook.row][rook.col] = None
        rook.row, rook.col = rook.row, new_col + 1
        board[rook.row][rook.col] = rook
    elif move == 'O-O':
        new_row, new_col = piece.row, piece.col + 2
        rook = board[piece.row][7]
        board[rook.row][rook.col] = None
        rook.row, rook.col = rook.row, new_col - 1
        board[rook.row][rook.col] = rook
    elif 'x' in move:
        new_row, new_col = coordinates[move[-2:]][0], coordinates[move[-2:]][1]
        if board[new_row][new_col] is None:
            cell = board[piece.row][new_col]
            
            board[piece.row][new_col] = None
        else:
            cell = board[new_row][new_col]
        print(cell.color, piece.color)
        print(move)
        GAME_PIECES[opposing_color(piece.color)].remove(cell)


    elif '=' in move:
        new_row, new_col = coordinates[move[2:-2]][0], coordinates[move[2:-2]][1]
        promote_to = move[-1]
        GAME_PIECES[piece.color].remove(piece)
        if promote_to == 'Q':
            piece = Queen(move[2:-2], piece.color, board)
        elif promote_to == 'R':
            piece = Rook(move[2:-2], piece.color, board)
        elif promote_to == 'B':
            piece = Bishop(move[2:-2], piece.color, board)
        elif promote_to == 'N':
            piece = Knight(move[2:-2], piece.color, board)
        GAME_PIECES[piece.color].append(piece)

    new_row, new_col = coordinates[move[-2:]][0], coordinates[move[-2:]][1]


    piece.move_count += 1
    board[new_row][new_col] = piece
    piece.row, piece.col = new_row, new_col
    last_move = piece.last_move
    piece.last_move = current_turn
    
    return [cell, last_move]

def UnmakeMove(move, moves, something):
    piece = moves[move]
    board[piece.row][piece.col] = None
    

    if move == 'O-O-O':
        old_row, old_col = piece.row, piece.col + 2
        rook = board[piece.row][piece.col + 1]
        board[rook.row][rook.col] = None
        rook.row, rook.col = rook.row, 0
        board[rook.row][rook.col] = rook
    elif move == 'O-O':
        old_row, old_col = piece.row, piece.col - 2
        rook = board[piece.row][7]
        board[rook.row][rook.col] = None
        rook.row, rook.col = rook.row, 7
        board[rook.row][rook.col] = rook
    elif 'x' in move:
        board[something[0].row][something[0].col] = something[0]
        
    elif '=' in move:
        
        old_row, old_col = coordinates[move[:2]][0], coordinates[move[:2]][1]
        GAME_PIECES[piece.color].remove(piece)
        piece = Pawn(move[:2], piece.color, board)
        piece.move_count = 6
        GAME_PIECES[piece.color].append(piece)


    if 'R' in move or 'N' in move or 'K' in move or 'B' in move or 'Q' in move:
        old_row, old_col = coordinates[move[1:3]][0], coordinates[move[1:3]][1]
    else:
        old_row, old_col = coordinates[move[:2]][0], coordinates[move[:2]][1]
    
    piece.move_count -= 1
    board[old_row][old_col] = piece
    piece.row, piece.col = old_row, old_col
    piece.last_move = something[1]

    
    return True



def CountPossiblePositions(depth, current_turn, thr, pieces):
    if depth == 0:
        return 1

    moves = safe_move(board, pieces, thr, current_turn)

    numPositions = 0
    for move in moves:
        something = MakeMove(move, moves, current_turn)
        f.write('\t' * current_turn + move)
        f.write('\n')
        thre = collect_threats(board, GAME_PIECES[pieces[0].color], thr, TURN_COUNTER)
        nodes = CountPossiblePositions(depth - 1, current_turn + 1, thre, GAME_PIECES[opposing_color(pieces[0].color)])
        numPositions += nodes
        UnmakeMove(move, moves, something)
        
    return numPositions


TURN_COUNTER = 0
board = [[None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]]

    
    
    
        


def specify_dual_figure_moves(first_piece_moves, second_piece_moves, move):
    # Если две фигуры могут сделать одно и тоже движение - надо указать ряд или колонку
    # Эта функция переделает возможные ходы для таких фигур
    first_piece = first_piece_moves[move]
    second_piece = second_piece_moves[move]
    if first_piece.col == second_piece.col:
        first_piece_move = move[0] + get_number(first_piece.row) + move[1:]
        second_piece_move = move[0] + get_number(second_piece.row) + move[1:]
    else:
        first_piece_move = move[0] + get_letter(first_piece.col) + move[1:]
        second_piece_move = move[0] + get_letter(second_piece.col) + move[1:]
    del first_piece_moves[move]
    del second_piece_moves[move]
    first_piece_moves[first_piece_move] = first_piece
    second_piece_moves[second_piece_move] = second_piece
    return True


def collect_threats(board, enemy_pieces, my_threats, current_turn): # my_threats - угрозы своего цвета
    real_threats = set() # вражеские угрозы
    for piece in enemy_pieces:
        piece.possible_moves(board, my_threats, current_turn)
        for real_threat in piece.threats:
            real_threats.add(real_threat)
    return sorted(real_threats) # возвращает вражеские угрозы


            
def safe_move(board, pieces, thr, current_turn):
    # Эта функция убирает ходы, которые позволяют съесть короля
    moves = {}
    for piece in pieces:
        piece_moves = piece.possible_moves(board, thr, current_turn)
        # for move in moves.copy():
        #     if move in piece_moves and moves[move] is not piece:
        #         # print(move, piece.col, moves[move].col)
        #         specify_dual_figure_moves(moves, piece_moves, move)
        #         # print(moves, '\n' ,piece_moves)
        moves = moves | piece_moves
    for move in moves.copy():
    
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
        piece.move_count += 1
        current_turn += 1  # Virtual turn

        board[new_row][new_col] = piece

        if 'x' in move and board[new_row][new_col] is None:
            if board[new_row][new_col] is None:
                cell = board[old_row][new_col]
                GAME_PIECES[opposing_color(piece.color)].remove(cell)
                new_row = old_row
            else:
                GAME_PIECES[opposing_color(piece.color)].remove(cell)
        thre = collect_threats(board, GAME_PIECES[opposing_color(piece.color)], thr, current_turn)
        if kings[piece.color].under_check(thre):
            del moves[move]
# возвращаем все не место
        piece.row = old_row
        piece.col = old_col
        board[new_row][new_col] = cell
        board[old_row][old_col] = piece
        piece.move_count -= 1
        current_turn -= 1
        if '=' in move:
            pieces.remove(piece)
            del piece
            pieces.append(return_piece)
            return_piece.row = old_row
            return_piece.col = old_col
            board[new_row][new_col] = cell
            board[old_row][old_col] = return_piece
        if 'x' in move and cell is not None:
            GAME_PIECES[opposing_color(piece.color)].append(cell)
    return moves
                
    
    


    

def move_piece(board, pieces, thr, current_turn):
    # эта функция двигает фигуру, если был введен правильный ход и возвращает True
    # если ход введен неверно, то функция вернет False

    moves = safe_move(board, pieces, thr, current_turn)
    if moves: # если ходов нет, то программа заканчивает работу
        actual_move = input()
                
        if actual_move in moves:
            piece = moves[actual_move]
            board[piece.row][piece.col] = None
            if actual_move == 'O-O-O':
                piece.row = piece.row
                piece.col = piece.col - 2
                piece.move_count += 1
                piece.last_move = current_turn
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
                piece.last_move = current_turn
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
                    GAME_PIECES[board[old_row][new_col].color].remove(board[old_row][new_col])
                    board[old_row][new_col] = None
                else:
                    GAME_PIECES[board[new_row][new_col].color].remove(board[new_row][new_col])


            piece.row = new_row
            piece.col = new_col
            board[new_row][new_col] = piece
            piece.move_count += 1
            piece.last_move = current_turn

            return True 
        return False
    else:
        print('Mate/Stalemate!')
        sys.exit()
        

    
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

# # white rooks
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

GAME_PIECES = {Color.WHITE: [], Color.BLACK: []}
kings = {Color.WHITE: king_w, Color.BLACK: king_b}

for line in board:
    for cell in line:
        if cell is not None:
            GAME_PIECES[cell.color].append(cell)


def print_board(board):
    
    print('+----+----+----+----+----+----+----+----+')
    for line in board:
        for cell in line:
            if cell is not None:
                if cell.color == 0:
                    print(f'| \033[33m{cell.name}\033[0m ', end=' ')
                else:
                    print(f'| \033[32m{cell.name}\033[0m ', end=' ')
            else:
                print('|   ', end=' ')
        print('|\n+----+----+----+----+----+----+----+----+')
    print()

cnt = 0
game = True

black_threats = collect_threats(board, GAME_PIECES[Color.BLACK], my_threats=[], current_turn=TURN_COUNTER) # угроза черных на 1 ход

turn = False
f = open('positions.txt', 'a')
print(CountPossiblePositions(4, TURN_COUNTER, black_threats, GAME_PIECES[Color.WHITE]))
f.close()
print(len(GAME_PIECES[Color.BLACK]), len(GAME_PIECES[Color.WHITE]))
sys.exit()
while game:
    print('+----+----+----+----+----+----+----+----+')
    for line in board:
        for cell in line:
            if cell is not None:
                if cell.color == 0:
                    print(f'| \033[33m{cell.name}\033[0m ', end=' ')
                else:
                    print(f'| \033[32m{cell.name}\033[0m ', end=' ')
            else:
                print('|   ', end=' ')
        print('|\n+----+----+----+----+----+----+----+----+')
    print()
    if turn == False and move_piece(board, GAME_PIECES[Color.WHITE], black_threats, TURN_COUNTER):
        turn = True
        white_threats = collect_threats(board, GAME_PIECES[Color.WHITE], black_threats, TURN_COUNTER)
    elif turn == True and move_piece(board, GAME_PIECES[Color.BLACK], white_threats, TURN_COUNTER):
        turn = False
        black_threats = collect_threats(board, GAME_PIECES[Color.BLACK], white_threats, TURN_COUNTER)
    else:
        print('---= Impossible move! =--- \n \t   or\n---= Incorrect input! =---')
    TURN_COUNTER += 1


