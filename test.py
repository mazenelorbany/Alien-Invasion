import pygame
import sys

pygame.init()

winSize = (600, 400)

displayScreen = pygame.display.set_mode(winSize)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
