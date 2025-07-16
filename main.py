"""test"""

import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((1024, 800))
clock = pygame.time.Clock()

# Load background image (make sure it's wide enough to scroll)
bg = pygame.image.load("background.png").convert()
bg_width = bg.get_width()

# Set initial scroll
scroll = 0
scroll_speed = 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Scroll background in the opposite direction
    scroll += scroll_speed
    if scroll < -bg_width:
        scroll = 0

    # Draw two copies of the background side-by-side
    screen.blit(bg, (scroll, 0))
    screen.blit(bg, (scroll + bg_width, 0))

    pygame.display.update()
    clock.tick(60)
