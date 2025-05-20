import pygame
import sys

# Initialize Pygame
pygame.init()

# Create game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Super Mario")

# Colors
background_color = (0, 150, 255)
ground_color = (255, 0, 0)
enemy_color = (0, 0, 0)

# Load Mario image
mario_img = pygame.image.load("assets/mario.png")
mario_img = pygame.transform.scale(mario_img, (200, 200))
mario_rect = mario_img.get_rect()
mario_rect.topleft = (100, 400)

# Ground setup
ground = pygame.Rect(0, 550, 800, 50)

# Movement and physics
speed = 5
gravity = 1
mario_y_speed = 0
is_jumping = False
jump_strength = -15

# Enemy setup
enemy = pygame.Rect(300, 500, 50, 50)
enemy_speed = 1

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)  # Limit to 60 FPS

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and mario_rect.left > 0:
        mario_rect.x -= speed
    if keys[pygame.K_RIGHT] and mario_rect.right < 800:
        mario_rect.x += speed
    if keys[pygame.K_SPACE] and not is_jumping:
        mario_y_speed = jump_strength
        is_jumping = True

    # Apply gravity
    mario_y_speed += gravity
    mario_rect.y += mario_y_speed

    # Ground collision
    if mario_rect.bottom >= ground.top:
        mario_rect.bottom = ground.top
        mario_y_speed = 0
        is_jumping = False

    # Enemy movement
    enemy.x += enemy_speed
    if enemy.right >= 800 or enemy.left <= 0:
        enemy_speed = -enemy_speed

    # Drawing
    screen.fill(background_color)
    pygame.draw.rect(screen, ground_color, ground)  # Draw ground
    pygame.draw.rect(screen, enemy_color, enemy)    # Draw enemy
    screen.blit(mario_img, mario_rect)              # Draw Mario

    pygame.display.update()

# Quit game
pygame.quit()
sys.exit()

