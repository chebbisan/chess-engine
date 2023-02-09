def get_coordinate(coordinate):
    for key in coordinates.keys():
        if coordinates[key] == coordinate:
            return key

coordinates = {'a8': (0, 0), 'b8': (0, 1), 'c8': (0, 2), 'd8': (0, 3), 'e8': (0, 4), 'f8': (0, 5), 'g8': (0, 6), 'h8': (0, 7),
    'a7': (1, 0), 'b7': (1, 1), 'c7': (1, 2), 'd7': (1, 3), 'e7': (1, 4), 'f7': (1, 5), 'g7': (1, 6), 'h7': (1, 7),
    'a6': (2, 0), 'b6': (2, 1), 'c6': (2, 2), 'd6': (2, 3), 'e6': (2, 4), 'f6': (2, 5), 'g6': (2, 6), 'h6': (2, 7),
    'a5': (3, 0), 'b5': (3, 1), 'c5': (3, 2), 'd5': (3, 3), 'e5': (3, 4), 'f5': (3, 5), 'g5': (3, 6), 'h5': (3, 7),
    'a4': (4, 0), 'b4': (4, 1), 'c4': (4, 2), 'd4': (4, 3), 'e4': (4, 4), 'f4': (4, 5), 'g4': (4, 6), 'h4': (4, 7),
    'a3': (5, 0), 'b3': (5, 1), 'c3': (5, 2), 'd3': (5, 3), 'e3': (5, 4), 'f3': (5, 5), 'g3': (5, 6), 'h3': (5, 7),
    'a2': (6, 0), 'b2': (6, 1), 'c2': (6, 2), 'd2': (6, 3), 'e2': (6, 4), 'f2': (6, 5), 'g2': (6, 6), 'h2': (6, 7),
    'a1': (7, 0), 'b1': (7, 1), 'c1': (7, 2), 'd1': (7, 3), 'e1': (7, 4), 'f1': (7, 5), 'g1': (7, 6), 'h1': (7, 7),}

class WhitePawn:
    def __init__(self, position):
        self.row = coordinates[position][0]
        self.col = coordinates[position][1]
        self.color = 1 # white

    def possible_moves(self, board):
        moves = []
        if self.row - 1 >= 0 and board[self.row - 1][self.col] == 0:
            moves.append(get_coordinate((self.row - 1, self.col)))
            if self.row == 6 and board[self.row - 2][self.col] == 0 and moves:
                moves.append(get_coordinate((self.row - 2, self.col)))
        return moves

    def move(self, board):
        return self.possible_moves(board)

    def possible_captures(self, board):
        captures = []
        p_captures = [(-1, -1), (-1, 1)]
        for p_capture in p_captures:
            new_row = self.row + p_capture[0]
            new_col = self.col + p_capture[1]
            if new_row >= 0 and 0 >= new_col >= 7:
                if board[new_row][new_col] == -1:
                    captures.append('x'.join([get_coordinate((self.row, self.col))[0], get_coordinate((new_row, new_col))]))
        return captures

    def capture(self, board):
        return self.possible_captures(board)



class BlackPawn:
    def __init__(self, position):
        self.row = coordinates[position][0]
        self.col = coordinates[position][1]
        self.color = -1 # black

    def possible_moves(self, board):
        moves = []
        if self.row + 1 <= 7 and board[self.row + 1][self.col] == 0:
            moves.append(get_coordinate((self.row + 1, self.col)))
            if self.row == 1 and board[self.row + 2][self.col] == 0 and moves:
                moves.append(get_coordinate((self.row + 2, self.col)))
        return moves

    def move(self, board):
        return self.possible_moves(board)

    def possible_captures(self, board):
        captures = []
        p_captures = [(1, -1), (1, 1)]
        for p_capture in p_captures:
            new_row = self.row + p_capture[0]
            new_col = self.col + p_capture[1]
            if new_row <= 7 and 0 >= new_col >= 7:
                if board[new_row][new_col] == 1:
                    captures.append('x'.join([get_coordinate((self.row, self.col))[0], get_coordinate((new_row, new_col))]))
        return captures

    def capture(self, board):
        return self.possible_captures(board)