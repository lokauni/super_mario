import pygame
import sys

#Initialize pygame
pygame.init()

#Creat game window
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Super Mario")

#Background color
b = (0, 150, 255)

#Load mario image
mario_img = pygame.image.load("assets/mario.png")
mario_img = pygame.transform.scale(mario_img, (200, 200))
rect = mario_img.get_rect()
rect.topleft = (100, 400)

#Earth
ground = pygame.Rect(0, 550, 800, 50)

#Speed mario
speed = 5

#Enemy
enemy = pygame.Rect(300, 500, 50, 50)
enemy_speed = 1

#Main game loop
while True:
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and rect.left > 0:
        rect.x -= speed
    if keys[pygame.K_RIGHT] and rect.right < 800:
        rect.x += speed

    enemy.x += enemy_speed
    if enemy.right >= 800 or enemy.left <= 0:
        enemy_speed = -enemy_speed

    screen.fill(b)
    pygame.draw.rect(screen, (255, 0, 0), ground)
    pygame.draw.rect(screen,(0, 0, 0), enemy)
    screen.blit(mario_img, rect)
    pygame.display.update()

