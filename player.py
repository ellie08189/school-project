"""Player sprite module."""

# pylint: disable=no-member

import pygame
from constants import PLAYER_SIZE, WIDTH, HEIGHT, PLAYER_SPEED


class Player(pygame.sprite.Sprite):
    """Player sprite controlled by arrow keys, drawn as a simple stick man."""

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE), pygame.SRCALPHA)
        self._draw_stick_man()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speed = PLAYER_SPEED

    def _draw_stick_man(self):
        """Draw a simple stick man figure on self.image."""
        black = (0, 0, 0)
        center_x = PLAYER_SIZE // 2
        head_radius = 6
        body_length = 12
        arm_length = 8
        leg_length = 10

        # Head (circle)
        pygame.draw.circle(
            self.image, black, (center_x, head_radius + 2), head_radius, 2
        )

        # Body (line)
        start_body = (center_x, head_radius * 2 + 2)
        end_body = (center_x, head_radius * 2 + 2 + body_length)
        pygame.draw.line(self.image, black, start_body, end_body, 2)

        # Arms (line)
        arm_y = head_radius * 2 + 6
        pygame.draw.line(
            self.image,
            black,
            (center_x - arm_length, arm_y),
            (center_x + arm_length, arm_y),
            2,
        )

        # Legs (lines)
        pygame.draw.line(
            self.image,
            black,
            end_body,
            (center_x - leg_length, end_body[1] + leg_length),
            2,
        )
        pygame.draw.line(
            self.image,
            black,
            end_body,
            (center_x + leg_length, end_body[1] + leg_length),
            2,
        )

    def update(self, keys_pressed):
        """Update the player position based on key presses."""
        if keys_pressed[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys_pressed[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys_pressed[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys_pressed[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
