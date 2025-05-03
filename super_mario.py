import pygame
import sys

#Initialize pygame
pygame.init()

#Creat game window
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Super Mario")

#Main game loop
while True:
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((135, 206, 235))
    pygame.display.update()
