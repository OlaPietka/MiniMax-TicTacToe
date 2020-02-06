from game.cell_type import Type
from copy import copy


class Ai:
    def __init__(self):
        pass

    def algorithm(self, s, depth, player):
        state = copy(s)
        if player == Type.X:
            best = [(-1, -1), -100]
        else:
            best = [(-1, -1), 100]

        if state.is_end() or depth == 0:
            value = self.evaluate(state, depth)
            return [(-1, -1), value]

        for cell in self.empty_cells(state):
            i, j = cell
            state.board.set_cell_type(i, j, player)
            state.round += 1
            score = self.algorithm(state, depth - 1, Type.X if player == Type.O else Type.O)
            state.board.set_cell_type(i, j, Type.EMPTY)
            state.round -= 1
            score[0] = (i, j)

            if player == Type.X:
                if score[1] > best[1]:
                    best = score
            else:
                if score[1] < best[1]:
                    best = score
            print("best:", best[1], "player:", player)
        return best

    def evaluate(self, state, depth):
        if state.winner is Type.X:
            return 10 - depth
        elif state.winner is Type.O:
            return -10 + depth
        else:
            return 0

    def empty_cells(self, state):
        cells = []

        for i, row in enumerate(state.board.cells):
            for j, cell in enumerate(row):
                if cell == Type.EMPTY:
                    cells.append((i, j))

        return cells
