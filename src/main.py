
import pygame
import random

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

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
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2
        self.speed = 5

# Define the Island class
class Island(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([100, 60])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Main menu function
def main_menu():
    button_font = pygame.font.SysFont(None, 48)
    label = button_font.render("Start Game", True, RED)
    button_rect = pygame.Rect((SCREEN_WIDTH - 200) // 2, (SCREEN_HEIGHT - 50) // 2, 200, 50)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    game_loop()

        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, button_rect)
        screen.blit(label, (button_rect.x + 25, button_rect.y + 10))
        
        pygame.display.flip()
        clock.tick(60)

# In-game menu function
def in_game_menu():
    paused = True
    pause_font = pygame.font.SysFont(None, 72)
    label = pause_font.render("Paused", True, RED)
    
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False

        screen.fill(WHITE)
        screen.blit(label, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 40))
        pygame.display.flip()
        clock.tick(60)

# Game loop function
def game_loop():
    ship = Ship()
    islands = pygame.sprite.Group()
    
    for _ in range(5):
        island = Island(random.randint(0, SCREEN_WIDTH-100), random.randint(0, SCREEN_HEIGHT-60))
        islands.add(island)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_UP]:
            dy = ship.speed
        if keys[pygame.K_DOWN]:
            dy = -ship.speed
        if keys[pygame.K_LEFT]:
            dx = ship.speed
        if keys[pygame.K_RIGHT]:
            dx = -ship.speed
        
        for island in islands:
            island.rect.x += dx
            island.rect.y += dy

        # In-game menu
        if keys[pygame.K_ESCAPE]:
            in_game_menu()

        screen.fill(WHITE)
        islands.draw(screen)
        screen.blit(ship.image, ship.rect)
        
        pygame.display.flip()
        clock.tick(60)

# Start with the main menu
main_menu()
pygame.quit()
