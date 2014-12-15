import pygame
from pygame.locals import *

WINDOW_SIZE = (1280,960)
BLOCK_SIZE = (WINDOW_SIZE[0]/32,WINDOW_SIZE[1]/20)
BLACK = pygame.Color('black')
WHITE = pygame.Color('White')
CYAN = pygame.Color('cyan')
YELLOW = pygame.Color('yellow')

######################################################################################################################### 

class Block(object):
        def __init__(self, color = CYAN , pos = (0,0)):
                (self.x , self.y) = pos
                self.pos = pos
                self.color = color

        def draw(self, display, row, colum):
                pos = ( BLOCK_SIZE[0]*colum , BLOCK_SIZE[1]*row )
                pygame.draw.rect(display, self.color , (BLOCK_SIZE[0]*colum,BLOCK_SIZE[1]*row,BLOCK_SIZE[0],BLOCK_SIZE[1]))

#########################################################################################################################

class Player(object):
        def __init__(self, radius = 10, color = YELLOW, pos = (WINDOW_SIZE[0]/32*2-20,WINDOW_SIZE[1]/20*19-24)):
                (self.x , self.y) = pos
                self.pos = pos
                self.radius = radius
                self.color = color
                self.canmoveup = True
                self.canmovedown = True
                self.canmoveright = True
                self.canmoveleft = True

        def move_up(self,delta_t):
                self.y -= 100*delta_t

        def move_down(self,delta_t):
                self.y += 100*delta_t

        def move_right(self,delta_t):
                self.x += 100*delta_t

        def move_left(self,delta_t):
                self.x -= 100*delta_t

        def move(self,delta_t):
                key = pygame.key.get_pressed()
                if key[K_UP] and self.canmoveup :
                        self.move_up(delta_t)
                elif key[K_DOWN] and self.canmovedown :
                        self.move_down(delta_t)
                elif key[K_RIGHT] and self.canmoveright :
                        self.move_right(delta_t)
                elif key[K_LEFT] and self.canmoveleft :
                        self.move_left(delta_t)

        def draw(self, display):
                pos = (int(self.x),int(self.y))
                pygame.draw.circle(display, self.color, pos, self.radius, 0 )

#########################################################################################################################
