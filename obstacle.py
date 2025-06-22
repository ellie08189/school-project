"""Obstacle module."""

# pylint: disable=no-member

import random
import pygame
from constants import OBSTACLE_WIDTH, OBSTACLE_HEIGHT, HEIGHT, OBSTACLE_SPEED, RED


def spawn_obstacle():
    """Create an obstacle rectangle at a random vertical position off screen."""
    y = random.randint(20, HEIGHT - 60)
    rect = pygame.Rect(0 - OBSTACLE_WIDTH, y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
    return rect


def move_and_draw_obstacles(screen, obstacles):
    """Move obstacles, draw them, and remove if off screen."""
    for obstacle in obstacles[:]:
        obstacle.x += OBSTACLE_SPEED
        pygame.draw.rect(screen, RED, obstacle)
        if obstacle.left > screen.get_width():
            obstacles.remove(obstacle)
