"""Main game loop."""

# pylint: disable=no-member

import sys
import pygame
from constants import WIDTH, HEIGHT, WHITE, BLACK, FPS
from player import Player
from obstacle import spawn_obstacle, move_and_draw_obstacles

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move the Man - Avoid Obstacles")
clock = pygame.time.Clock()


def main():
    """Run the game."""
    player = Player()
    obstacles = []
    spawn_timer = 0
    spawn_interval = 90  # frames

    running = True
    game_over = False

    while running:
        clock.tick(FPS)
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not game_over:
            keys = pygame.key.get_pressed()
            player.update(keys)

            spawn_timer += 1
            if spawn_timer >= spawn_interval:
                spawn_timer = 0
                obstacles.append(spawn_obstacle())

            move_and_draw_obstacles(screen, obstacles)

            if any(player.rect.colliderect(obstacle) for obstacle in obstacles):
                game_over = True

            screen.blit(player.image, player.rect)

        else:
            font = pygame.font.SysFont(None, 48)
            text = font.render("Game Over! Close window to exit.", True, BLACK)
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(text, text_rect)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
