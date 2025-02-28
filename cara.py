# import the pygame module, so you can use it
# import pygame, sys


CAPTION_TEXT = "LOLA INDITEX"
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
INDIGO = (75, 0, 130)
ORANGE = (255, 165, 0)
YELLOW = (255,255,0)
VIOLET = (148,0,211)
GREY = (128,128,128)
MARRON = (128,0,0)
BLACK = (0,0,0)
OLIVE = (134,139,73)
CYAN = (0,255,255)
PINK = (255,153,204)
MAGENTA = (255,0,255)
TAN = (210,180,140)
TEAL = (0,128,128)
WHITE = (255,255,255)
color = TEAL
import pygame, sys
from pygame.locals import *

pygame.init()
pantalla = pygame.display.set_mode((850,850))
pygame.display.set_caption('Calamardo')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill(BLACK)
    pygame.draw.circle(pantalla, TEAL, (425,250), 200)
    rectangle1 = pygame.Rect(350,230,155,350)
    pygame.draw.rect(pantalla, TEAL, rectangle1)
    pygame.draw.ellipse(pantalla, TEAL, (235, 470, 400, 120))
    pygame.draw.rect(pantalla, TEAL, (385, 585, 80, 800))
    pygame.draw.rect(pantalla, BLACK, (385, 665, 80, 800))
    pygame.draw.line(pantalla, BLACK, (300, 520), (560, 520), 10)
    pygame.draw.ellipse(pantalla, CYAN, (380, 380, 100, 225))
    pygame.draw.ellipse(pantalla, WHITE, (310, 230, 90, 140))
    pygame.draw.ellipse(pantalla, WHITE, (450, 230, 90, 140))
    pygame.draw.rect(pantalla, RED, (345, 270, 20, 90))
    pygame.draw.rect(pantalla, RED, (485, 270, 20, 90))
    pygame.draw.rect(pantalla, CYAN, (310, 255, 90, 45))
    pygame.draw.rect(pantalla, CYAN, (450, 255, 90, 45))
    pygame.draw.circle(pantalla, CYAN, (355, 250), 45)
    pygame.draw.circle(pantalla, CYAN, (495, 250), 45)

    pygame.display.update()
