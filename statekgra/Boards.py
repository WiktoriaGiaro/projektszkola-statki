import pygame

width=340
height=340

class Player_board:
    def __init__(self):
        self.ship = []
        self.surf = pygame.Surface((width, height))
        self.surf.fill((128,128,128))
        grid_width = 30
        grid_height = 30
        for i in range(20, width - 20, grid_width):
            for x in range(20, height - 20, grid_height):
                rect = pygame.Rect((i, x), (grid_width, grid_height))
                pygame.draw.rect(self.surf, (0, 0, 0), rect, 1)
class AI_board:
    def __init__(self):
        self.ship = []
        self.surf = pygame.Surface((width, height))
        self.surf.fill((128,128,128))
        grid_width = 30
        grid_height = 30
        for i in range(20, width - 20, grid_width):
            for x in range(20, height - 20, grid_height):
                rect = pygame.Rect((i, x), (grid_width, grid_height))
                pygame.draw.rect(self.surf, (0, 0, 0), rect, 1)
