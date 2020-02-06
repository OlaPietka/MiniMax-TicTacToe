from game.cell_type import Type


class Board:
    def __init__(self):
        self.cells = [[Type.EMPTY for i in range(3)] for j in range(3)]

    def get_cell_type(self, i, j):
        return self.cells[i][j]

    def set_cell_type(self, i, j, type):
        self.cells[i][j] = type

    def to_string(self):
        s = ""
        for row in self.cells:
            for cell in row:
                if cell is Type.EMPTY:
                    s += "-"
                elif cell is Type.O:
                    s += "O"
                else:
                    s += "X"
            s += "\n"
        print(s)
