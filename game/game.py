from game.board import Board
from game.cell_type import Type


class Game:
    def __init__(self):
        self.board = Board()
        self.round = 0
        self.winner = None
        self.x_points = 0
        self.o_points = 0

    def new(self):
        self.board = Board()
        self.round = 0
        self.winner = None

    def is_end(self):
        cross1 = []
        cross2 = []

        for i in range(3):
            row = [type for type in self.board.cells[i]]
            col = [row[i] for row in self.board.cells]

            cross1.append(self.board.get_cell_type(i, i))
            cross2.append(self.board.get_cell_type(i, 2 - i))

            for t in [Type.O, Type.X]:
                if row == [t] * 3 or col == [t] * 3 or cross1 == [t] * 3 or cross2 == [t] * 3:
                    self.winner = t
                    return True

        if self.winner is not None and self.round == 9:
            self.winner = Type.EMPTY
            return True

        return False

    def add_points_to_winner(self):
        if self.winner is Type.EMPTY:
            return

        if self.winner is Type.X:
            self.x_points += 1
        else:
            self.o_points += 1

    def get_current_player(self):
        return Type.O if self.round % 2 == 0 else Type.X
