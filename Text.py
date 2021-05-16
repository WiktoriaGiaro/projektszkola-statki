import random
import Boards
import pygame
from pygame import *
from Menu import *
from battleship import *


pygame.font.init()
height = 680
width = 680
screen = pygame.display.set_mode((width, height))

class Text_Display():
    def __init__(self, font, size, text, antialias, color, background):
        self.font=font
        self.size=size
        self.text=text
        self.antialias = antialias
        self.color=color
        self.background=background
        texts=pygame.font.SysFont(self.font, self.size)
        self.text=texts.render(self.text, self.antialias, self.color)
    def blit_text(self):
        screen.blit(self.text, (width//5, 570))