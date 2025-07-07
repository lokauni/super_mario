import pygame
import sys

# Initialize Pygame
pygame.init()

# Create game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Super Mario")

# Colors
text_color = (255, 255, 255)      # White (Text)

# Load Mario image
mario_img = pygame.image.load("assets/mario.png")
mario_img = pygame.transform.scale(mario_img, (120, 140))
mario_rect = mario_img.get_rect()
mario_rect.topleft = (100, 380)

# Load coin image
coin_img = pygame.image.load("assets/coin.png")
coin_img = pygame.transform.scale(coin_img, (70, 70))

# Load brick platform image
brick_img = pygame.image.load("assets/brick.png")
brick_img = pygame.transform.scale(brick_img, (190, 50))

#Load enemy image
enemy_img = pygame.image.load("assets/enemy.webp")
enemy_img = pygame.transform.scale(enemy_img, (80, 80))

#Load background image
background_img = pygame.image.load("assets/background.jpg")
background_img = pygame.transform.scale(background_img, (800, 600))

# Ground setup
ground = pygame.Rect(0, 550, 800, 50)

# Platforms setup
platforms = [
    pygame.Rect(200, 390, 150, 20),
    pygame.Rect(400, 340, 150, 20),
    pygame.Rect(250, 290, 150, 20),
    pygame.Rect(450, 240, 150, 20)
]

# Coins setup (centered on some platforms)
coins = [
    pygame.Rect(260, 360, 20, 20),
    pygame.Rect(460, 310, 20, 20),
    pygame.Rect(300, 260, 20, 20),
    pygame.Rect(500, 210, 20, 20)
]

# Movement and physics
speed = 5
gravity = 1
mario_y_speed = 0
is_jumping = False
jump_strength = -35

# Enemy setup
enemy = pygame.Rect(730, 500, 50, 50)
enemy_speed = -1

# Clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    clock.tick(60)

    # Events
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

    # Prevent Mario from going above the screen
    if mario_rect.top < 0:
        mario_rect.top = 0
        mario_y_speed = 0

    # Platform collision
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

    # Enemy collision
    if mario_rect.colliderect(enemy):
        font = pygame.font.SysFont(None, 100)
        game_over_text = font.render("GAME OVER", True, text_color)
        screen.blit(game_over_text, (250, 250))
        pygame.display.update()
        pygame.time.delay(2000)
        running = False

    # Coin collection
    collected_coins = []
    if on_platform:
        for coin in coins:
            if mario_rect.colliderect(coin):
                collected_coins.append(coin)
    for coin in collected_coins:
        coins.remove(coin)

    # Drawing
    screen.blit(background_img, (0, 0))

    # Draw platforms with brick image
    for platform in platforms:
        screen.blit(brick_img, (platform.x, platform.y))

    # Draw enemy
    screen.blit(enemy_img, (enemy.x, enemy.y))

    # Draw Mario
    screen.blit(mario_img, (mario_rect.x, mario_rect.y + 30))

    # Draw coins
    for coin in coins:
        screen.blit(coin_img, (coin.x, coin.y))

    pygame.display.update()

# Quit game
pygame.quit()
sys.exit()

