import pygame

from game.ai import Ai
from game.cell_type import Type
from game.game import Game
from game.screen import Screen


if __name__ == '__main__':
    pygame.init()
    screen = Screen()
    game = Game()
    ai = Ai()

    def new_game():
        game.add_points_to_winner()
        game.new()
        screen.new()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                i, j = screen.pixels_to_indexes(x, y)

                if game.board.get_cell_type(i, j) is Type.EMPTY:
                    current_player = game.get_current_player()

                    game.board.set_cell_type(i, j, current_player)
                    screen.add_image(i, j, current_player)
                    if game.is_end():
                        pygame.time.wait(1000)
                        new_game()
                    else:
                        game.round += 1

        screen.draw(game.x_points, game.o_points)

        if game.is_end():
            pygame.time.wait(1000)
            new_game()

        if game.round % 2 == 1:
            print("New-----")
            l = ai.algorithm(game, 10, Type.X)
            i, j = l[0]
            current_player = game.get_current_player()
            game.board.set_cell_type(i, j, current_player)
            screen.add_image(i, j, current_player)
            game.round += 1



