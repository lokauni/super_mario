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
platform_color = (0, 255, 0)
enemy_color = (0, 0, 0)

# Load Mario image
mario_img = pygame.image.load("assets/mario.png")
mario_img = pygame.transform.scale(mario_img, (120, 140))
mario_rect = mario_img.get_rect()
mario_rect.topleft = (350, 380)

# Ground setup
ground = pygame.Rect(0, 550, 800, 50)

#Platforms
platforms = [
        pygame.Rect(200, 450, 150, 20),
        pygame.Rect(400, 400, 150, 20),
        pygame.Rect(250, 350, 150, 20),
        pygame.Rect(450, 300, 150, 20)

]

# Movement and physics
speed = 5
gravity = 1
mario_y_speed = 0
is_jumping = False
jump_strength = -35

# Enemy setup
enemy = pygame.Rect(300, 500, 50, 50)
enemy_speed = 1

#Clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    clock.tick(60)  

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
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

    # Gravity
    mario_y_speed += gravity
    mario_rect.y += mario_y_speed

    #Prevent Mario from going above the screen
    if mario_rect.top < 0:
        mario_rect.top = 0
        mario_y_speed = 0

    
    #Platform collision
    on_platform = False
    for platform in platforms:
        if mario_rect.colliderect(platform):
            if mario_y_speed > 0 and mario_rect.bottom - mario_y_speed <= platform.top:
                mario_rect.bottom = platform.top
                mario_y_speed = 0
                is_jumping = False
                on_platform = True
                break
            
    # Ground collision
    if not on_platform and mario_rect.bottom >= ground.top:
        mario_rect.bottom = ground.top
        mario_y_speed = 0
        is_jumping = False


    # Enemy movement
    enemy.x += enemy_speed
    if enemy.right >= 800 or enemy.left <= 0:
        enemy_speed = -enemy_speed

    # Drawing
    screen.fill(background_color)
    pygame.draw.rect(screen, ground_color, ground)
    for platform in platforms:
        pygame.draw.rect(screen, platform_color, platform)
    pygame.draw.rect(screen, enemy_color, enemy)    
    screen.blit(mario_img,(mario_rect.x, mario_rect.y + 10))              

    pygame.display.update()

# Quit game
pygame.quit()
sys.exit()

