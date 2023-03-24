
def get_coordinate(coordinate):
    col = chr(ord('a') + coordinate[1])
    row = str(8 - coordinate[0])
    return col + row

def in_bounds(row, col):
        return row >= 0 and col >= 0 and row <= 7 and col <=7

def empty(board, row, col):
    return board[row][col] is None

coordinates = {'a8': (0, 0), 'b8': (0, 1), 'c8': (0, 2), 'd8': (0, 3), 'e8': (0, 4), 'f8': (0, 5), 'g8': (0, 6), 'h8': (0, 7),
    'a7': (1, 0), 'b7': (1, 1), 'c7': (1, 2), 'd7': (1, 3), 'e7': (1, 4), 'f7': (1, 5), 'g7': (1, 6), 'h7': (1, 7),
    'a6': (2, 0), 'b6': (2, 1), 'c6': (2, 2), 'd6': (2, 3), 'e6': (2, 4), 'f6': (2, 5), 'g6': (2, 6), 'h6': (2, 7),
    'a5': (3, 0), 'b5': (3, 1), 'c5': (3, 2), 'd5': (3, 3), 'e5': (3, 4), 'f5': (3, 5), 'g5': (3, 6), 'h5': (3, 7),
    'a4': (4, 0), 'b4': (4, 1), 'c4': (4, 2), 'd4': (4, 3), 'e4': (4, 4), 'f4': (4, 5), 'g4': (4, 6), 'h4': (4, 7),
    'a3': (5, 0), 'b3': (5, 1), 'c3': (5, 2), 'd3': (5, 3), 'e3': (5, 4), 'f3': (5, 5), 'g3': (5, 6), 'h3': (5, 7),
    'a2': (6, 0), 'b2': (6, 1), 'c2': (6, 2), 'd2': (6, 3), 'e2': (6, 4), 'f2': (6, 5), 'g2': (6, 6), 'h2': (6, 7),
    'a1': (7, 0), 'b1': (7, 1), 'c1': (7, 2), 'd1': (7, 3), 'e1': (7, 4), 'f1': (7, 5), 'g1': (7, 6), 'h1': (7, 7)}

class Figure:
    def has_enemy(self, board, row, col):
        return board[row][col] is not None and board[row][col].color != self.color
    
    def check(self, board, row, col):
        return isinstance(board[row][col], King)



class Pawn(Figure):
    def __init__(self, position, color, board):
        self.row = coordinates[position][0]
        self.col = coordinates[position][1]
        self.color = color # 0 - white, 1 - black
        board[self.row][self.col] = self
        self.threats = []
        self.move_count = 0
        self.name = 'P'

    def possible_moves(self, board, imp_moves):
        moves = []
        direction = -1 if self.color == 0 else 1
        p_captures = [(-1, -1), (-1, 1)] if self.color == 0 else [(1, -1), (1, 1)]
        self.threats = []

        if in_bounds(self.row + 1 * direction, self.col) and board[self.row + 1 * direction][self.col] is None:
            moves.append(get_coordinate((self.row + 1 * direction, self.col)))
            if self.move_count == 0 and in_bounds(self.row + 2 * direction, self.col) and board[self.row + 2 * direction][self.col] is None:
                moves.append(get_coordinate((self.row + 2 * direction, self.col)))

        for p_capture in p_captures:
            new_row = self.row + p_capture[0]
            new_col = self.col + p_capture[1]
            if in_bounds(new_row, new_col):
                self.threats.append(get_coordinate((new_row, new_col)))
                if self.has_enemy(board, new_row, new_col):
                    moves.append('x'.join([get_coordinate((self.row, self.col))[0], get_coordinate((new_row, new_col))]))
        return moves


    def move(self, board, imp_moves):
        return self.possible_moves(board, imp_moves)
    

    

class Rook(Figure):
    def __init__(self, position, color, board):
        self.row = coordinates[position][0]
        self.col = coordinates[position][1]
        self.color = color # 0 - white, 1 - black
        board[self.row][self.col] = self
        self.threats = []
        self.move_count = 0
        self.name = 'R'

    def possible_moves(self, board, imp_moves):
        moves = []
        self.threats = []

        steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for step in steps:
            new_row, new_col = self.row + step[0], self.col + step[1]
            while in_bounds(new_row, new_col):
                self.threats.append(get_coordinate((new_row, new_col)))
                if empty(board, new_row, new_col):
                    moves.append('R' + get_coordinate((new_row, new_col)))
                elif self.has_enemy(board, new_row, new_col):
                    moves.append('Rx' + get_coordinate((new_row, new_col)))
                    break
                else:
                    break
                new_row, new_col = new_row + step[0], new_col + step[1]
        return moves

    def move(self, board, imp_moves):
        return self.possible_moves(board, imp_moves)
    

class Bishop(Figure):
    def __init__(self, position, color, board):
        self.row = coordinates[position][0]
        self.col = coordinates[position][1]
        self.color = color # 0 - white, 1 - black
        board[self.row][self.col] = self
        self.threats = []
        self.move_count = 0
        self.name = 'B'

    def possible_moves(self, board, imp_moves):
        moves = []
        self.threats = []
        steps = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
        for step in steps:
            new_row, new_col = self.row + step[0], self.col + step[1]
            while in_bounds(new_row, new_col):
                self.threats.append(get_coordinate((new_row, new_col)))
                if empty(board, new_row, new_col):
                    moves.append('B' + get_coordinate((new_row, new_col)))
                elif self.has_enemy(board, new_row, new_col):
                    moves.append('Bx' + get_coordinate((new_row, new_col)))
                    break
                else:
                    break
                new_row, new_col = new_row + step[0], new_col + step[1]
        return moves

    def move(self, board, imp_moves):
        return self.possible_moves(board, imp_moves)
    

class Knight(Figure):
    def __init__(self, position, color, board):
        self.row = coordinates[position][0]
        self.col = coordinates[position][1]
        self.color = color # 0 - white, 1 - black
        board[self.row][self.col] = self
        self.threats = []
        self.move_count = 0
        self.name = 'N'

    def possible_moves(self, board, imp_moves):
        k_moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        moves = []
        self.threats = []
        for k_move in k_moves:
            new_row = self.row + k_move[0]
            new_col = self.col + k_move[1]
            if in_bounds(new_row, new_col):
                self.threats.append(get_coordinate((new_row, new_col)))
                if board[new_row][new_col] == None:
                    moves.append('N' + get_coordinate((new_row, new_col)))
                elif self.has_enemy(board, new_row, new_col):
                    moves.append('Nx' + get_coordinate((new_row, new_col)))
        return moves

    def move(self, board, imp_moves):
        return self.possible_moves(board, imp_moves)
    

class Queen(Figure):
    def __init__(self, position, color, board):
        self.row = coordinates[position][0]
        self.col = coordinates[position][1]
        self.color = color # 0 - white, 1 - black
        board[self.row][self.col] = self
        self.threats = []
        self.move_count = 0
        self.name = 'Q'

    def possible_moves(self, board, imp_moves):
        moves = []
        self.threats = []
        steps = [(1, 1), (-1, 1), (-1, -1), (1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]
        for step in steps:
            new_row, new_col = self.row + step[0], self.col + step[1]
            while in_bounds(new_row, new_col):
                self.threats.append(get_coordinate((new_row, new_col)))
                if empty(board, new_row, new_col):
                    moves.append('Q' + get_coordinate((new_row, new_col)))
                elif self.has_enemy(board, new_row, new_col):
                    moves.append('Qx' + get_coordinate((new_row, new_col)))
                    break
                else:
                    break
                new_row, new_col = new_row + step[0], new_col + step[1]
        return moves

    def move(self, board, imp_moves):
        return self.possible_moves(board, imp_moves)
    

class King(Figure):
    def __init__(self, position, color, board):
        self.row = coordinates[position][0]
        self.col = coordinates[position][1]
        self.color = color # 1 - white, -1 - black
        board[self.row][self.col] = self
        self.threats = []
        self.move_count = 0
        self.name = 'K'

    def possible_moves(self, board, imp_moves):


        p_moves = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        moves = []
        self.threats = []
        for p_move in p_moves:
            new_row = self.row + p_move[0]
            new_col = self.col + p_move[1]
            if in_bounds(new_row, new_col):
                self.threats.append(get_coordinate((new_row, new_col)))
                if board[new_row][new_col] == None and get_coordinate((new_row, new_col)) not in imp_moves:
                    moves.append('K' + get_coordinate((new_row, new_col)))
                elif self.has_enemy(board, new_row, new_col) and get_coordinate((new_row, new_col)) not in imp_moves:
                    moves.append('Kx' + get_coordinate((new_row, new_col)))
        return moves
    
    def can_castle(self, board, imp_moves):
        castle = []

        if self.move_count == 0:
            possible_rooks = [board[self.row][0], board[self.row][7]]
            for possible_rook, move, sign in zip(possible_rooks, ['O-O-O', 'O-O'], [-1, 1]):
                if isinstance(possible_rook, Rook) and possible_rook.move_count == 0 and possible_rook.color == self.color:
                    if self.has_space_for_castle(board, possible_rook):
                        if get_coordinate((self.row, self.col + 1 * sign)) not in imp_moves and get_coordinate((self.row, self.col + 2 * sign)) not in imp_moves:
                            castle.append(move)

        return castle

    
    def has_space_for_castle(self, board, rook):
        empty = True
        for i in range(min(rook.col, self.col) + 1, max(rook.col, self.col)):
            if board[self.row][i] is not None:
                empty = False
                break
        return empty
    
    def under_check(self, imp_moves):
        if get_coordinate((self.row, self.col)) in imp_moves:
            print('Check!')
            return True


    def move(self, board, imp_moves):
        return self.possible_moves(board, imp_moves) + self.can_castle(board, imp_moves)
