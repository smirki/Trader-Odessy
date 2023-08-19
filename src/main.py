import pygame
import random

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create screen and clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("IsleTrader Odyssey: Seafarer's Harvest")
clock = pygame.time.Clock()

# Define the Ship class
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 30])
        self.image.fill(BLUE)  # Temporary blue color, replace with your art later
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2
        self.speed = 5

    def move(self, x, y):
        self.rect.x += x * self.speed
        self.rect.y += y * self.speed

# Define the Island class
class Island(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([100, 60])
        self.image.fill(GREEN)  # Temporary green color, replace with your art later
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

ship = Ship()
all_sprites = pygame.sprite.Group()
all_sprites.add(ship)

# Create random islands
for _ in range(5):
    island = Island(random.randint(0, SCREEN_WIDTH-100), random.randint(0, SCREEN_HEIGHT-60))
    all_sprites.add(island)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ship.move(0, -1)
    if keys[pygame.K_DOWN]:
        ship.move(0, 1)
    if keys[pygame.K_LEFT]:
        ship.move(-1, 0)
    if keys[pygame.K_RIGHT]:
        ship.move(1, 0)

    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()