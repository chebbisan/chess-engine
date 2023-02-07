class Pawn:
    def __init__(self, col, row):
        self.col = col
        self.row = row
        self.move_count = 0

    def possible_moves(self):
        if self.move_count == 0 and self.row == 2:
            return [(self.col, self.row + 2), (self.col, self.row + 1)]
        if self.move_count == 7:
            return [] # здесь должна быть функция выбора фигуры и переход на последнюю горизонталь
        return [(self.col, self.row + 1)]

    def move(self):
        for move in self.possible_moves():
            print(move)
