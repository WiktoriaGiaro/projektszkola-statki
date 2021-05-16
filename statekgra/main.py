import random
import Boards
import pygame
from pygame import *
from Menu import *
from battleship import *
from Text import *

if __name__ == "__main__":
    while True:
        choice=Menu(screen).display()
        if choice==QUIT:
            False
        elif choice==LAUNCH_GAME:
            screen.blit(pygame.image.load('paperbackground.jpg'), (0, 0))
            text1.blit_text()
            AI_LOCATION()
            end_game()
            game()
            break
