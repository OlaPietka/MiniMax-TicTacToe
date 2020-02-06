# TicTacToe

## Description
Well known game with implemented MiniMax algorithm.

<p align="center">
  <img src="https://i.imgur.com/SgBeJaD.png">
</p>

## Algorithm
```python
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
```
