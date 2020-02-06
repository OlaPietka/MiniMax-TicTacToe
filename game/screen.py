import pygame


class Screen:
    def __init__(self):
        self.BOARD_SIZE = 300
        self.SCREEN_SIZE = (self.BOARD_SIZE, self.BOARD_SIZE + 100)
        self.CELL_SIZE = self.BOARD_SIZE // 3
        self.MARGIN = 1
        self.SCREEN = pygame.display.set_mode(self.SCREEN_SIZE)
        self.CELL_COLOR = (255, 255, 255)
        self.LINE_COLOR = (0, 0, 0)
        self.FONT_COLOR = (255, 255, 255)
        self.IMAGE_SIZE = int(0.8 * self.CELL_SIZE)
        self.FONT = pygame.font.SysFont('arial', 32)
        self.images = []

    def new(self):
        self.images = []

    def draw(self, x_points, o_points):
        self.SCREEN.fill(self.LINE_COLOR)

        for row in range(3):
            for col in range(3):
                coord = self.indexes_to_pixels(row, col)
                pygame.draw.rect(self.SCREEN, self.CELL_COLOR, (coord[0], coord[1], self.CELL_SIZE, self.CELL_SIZE))

        self.SCREEN.blits(self.images)

        self.SCREEN.blits(self.text(x_points, o_points))
        pygame.display.flip()

    def indexes_to_pixels(self, i, j):
        x = (self.CELL_SIZE + self.MARGIN) * i + self.MARGIN
        y = (self.CELL_SIZE + self.MARGIN) * j + self.MARGIN
        return x, y

    def pixels_to_indexes(self, x, y):
        i = x // (self.CELL_SIZE + self.MARGIN)
        j = y // (self.CELL_SIZE + self.MARGIN)
        return i, j

    def add_image(self, i, j, type):
        x, y = self.indexes_to_pixels(i, j)
        self.images.append((self.load_image("images/" + type.name),
                            (x + (self.CELL_SIZE - self.IMAGE_SIZE) / 2, y + (self.CELL_SIZE - self.IMAGE_SIZE) / 2)))

    def load_image(self, filename):
        img_load = pygame.image.load('{}.png'.format(filename))
        return pygame.transform.scale(img_load, (self.IMAGE_SIZE, self.IMAGE_SIZE))

    def text(self, x_points, o_points):
        x = self.BOARD_SIZE // 8
        y = self.SCREEN_SIZE[1] - 65
        return [(self.get_font_render("X: {}".format(str(x_points))), (x, y)),
                (self.get_font_render("O: {}".format(str(o_points))), (6 * x, y))]

    def get_font_render(self, string):
        return self.FONT.render(string, True, self.FONT_COLOR)
