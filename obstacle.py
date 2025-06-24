"""Obstacle module."""

# pylint: disable=no-member

import random
import pygame
from constants import OBSTACLE_WIDTH, OBSTACLE_HEIGHT, HEIGHT, OBSTACLE_SPEED, RED


def spawn_obstacle():
    """Create an obstacle rectangle at a random horizontal position, starting just above the screen."""
    x = random.randint(20, 800 - 60)  # Adjust 800 or use screen width
    rect = pygame.Rect(x, 0 - OBSTACLE_HEIGHT, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
    return rect


def move_and_draw_obstacles(screen, obstacles):
    """Move obstacles down, draw them, and remove if off screen."""
    for obstacle in obstacles[:]:
        obstacle.y += OBSTACLE_SPEED
        pygame.draw.rect(screen, RED, obstacle)

        if obstacle.top > HEIGHT:
            obstacles.remove(obstacle)
