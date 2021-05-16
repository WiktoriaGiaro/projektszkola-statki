import random
import Boards
import pygame
from pygame import *
from Menu import *
from Text import *

pygame.init()



def Calculate_rect(cord, origin):
    column = ((cord[0] - origin[0]) // 30)
    row = ((cord[1] - origin[1]) // 30)
    return [row, column]


def in_grid(row, column, align, size):
    if align=='h':
        if ((column + size + 1) <= 10):
            return True
    else:
        if ((row + size + 1) <= 10):
            return True
    return False

def check_if_elements_unique(my_list):
    for i in my_list:
        if my_list.count(i) > 1:
            return False
    return True

def AI_LOCATION():
    SHIP_LOCATION = []
    size = 5
    while size != 0:
        temp_list = []
        align=random.choice(('h', 'v'))
        row = random.choice(range(10))
        column = random.choice(range(10))
        if ([row, column] in SHIP_LOCATION) or (in_grid(row, column, align, size) == False):
            continue
        else:
            if align == 'h':
                for i in range(size):
                    temp_list.append([row, column + i])

                else:
                    SHIP_LOCATION.extend(temp_list)
                    size -= 1
            else:
                for i in range(size):
                    temp_list.append([row + i, column])

                else:
                    SHIP_LOCATION.extend(temp_list)
                    size -= 1
    ai.ship = SHIP_LOCATION

def game():
    number_phits = 0
    number_aihits = 0
    run = True

    while run:
        screen.blit(player.surf, (0, height // 4))
        screen.blit(ai.surf, (width // 2, height // 4))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==QUIT:
                run=False
            if event.type == pygame.MOUSEBUTTONUP:
                cord = event.pos
                if cord[0] >= 360 and cord[0] <= 660 and cord[1] >= 190 and cord[1] <= 490:
                    row = random.choice(range(10))
                    column = random.choice(range(10))
                    ai_rectangle = [row, column]
                    ai_x = (ai_rectangle[0] * 30) + 190
                    ai_y = (ai_rectangle[1] * 30) + 20
                    ai_rect = pygame.Rect((ai_y, ai_x - 20 - 150), (30, 30))
                    rectangle = Calculate_rect(cord, (360, 190))
                    player_x = (rectangle[0] * 30) + 190
                    player_y = (rectangle[1] * 30) + 20
                    playerrect = pygame.Rect((player_y, player_x - 20 - 150), (30, 30))
                    if rectangle in ai.ship:
                        pygame.draw.rect(ai.surf, (255, 0, 0), playerrect)
                        number_phits += 1

                    else:
                        pygame.draw.rect(ai.surf, (255, 255, 224), playerrect)
                    if ai_rectangle in player.ship:

                        pygame.draw.rect(player.surf, (255, 0, 0), ai_rect)
                        number_aihits += 1

                    else:
                        pygame.draw.rect(player.surf, (255, 255, 224), ai_rect)

        if number_phits==15:
            print("ZWYCIĘSTWO")
            if number_aihits<=5:
                score=number_phits*3
                with open('score.txt', 'a') as save:
                    save.write("Your score: " + str(score)+"\n")
                    print("Liczba punktów:", score)
            elif number_aihits>5 and number_aihits<=10:
                score=number_phits * 2
                with open('score.txt', 'a') as save:
                    save.write("Your score: " + str(score)+"\n")
                print("Liczba punktów:", number_phits*2)
            elif number_aihits>10 and number_aihits<=15:
                score=number_phits
                with open('score.txt', 'a') as save:
                    save.write("Your score: " + str(score)+"\n")
                    print("Liczba punktów:", score)
            break
        if number_aihits==15:
            print("przykro mi...")

            break


def end_game():

    SHIP_LOCATION = []
    ships = ["5", "4", "3", "2", "1"]
    colors = (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)
    run=True
    t=0
    count=0
    screen.blit(player.surf, (0, height // 4))
    pygame.display.flip()

    while run:
        if t>=5:
            break
        size=5-t
        color=colors[t]
        for event in pygame.event.get():
            if count >= size:
                t+=1
                count=0
                break
            if event.type==QUIT:
                run=False

            if event.type==pygame.MOUSEBUTTONUP and count<=size:
                rect = pygame.Rect((0, 50), (680, 50))
                cord = event.pos

                if cord[0]<=320 and cord[0]>=20 and cord[1]>=190 and cord[1]<=490:
                    rectangle=Calculate_rect(cord, (20, 190))
                    if rectangle not in SHIP_LOCATION:
                        count+=1
                        SHIP_LOCATION.append(rectangle)
                        x=(rectangle[0] * 30) + 190
                        y=(rectangle[1] * 30) + 20
                        rect=pygame.Rect((y, x), (30, 30))
                        rect_player=pygame.Rect((y, x - 20 - 150), (30, 30))
                        pygame.draw.rect(player.surf, color, rect_player)
                        pygame.draw.rect(screen, color, rect)
                        pygame.display.flip()
                    else:
                        pygame.display.flip()
                player.ship = SHIP_LOCATION



player = Boards.Player_board()
ai = Boards.AI_board()
text1 = Text_Display('Comic Sans MS', 30, "kolejność statków: 5, 4, 3, 2, 1", True, (0, 0, 0), None)
menu=Menu(screen)
