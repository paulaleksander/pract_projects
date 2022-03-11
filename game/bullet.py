import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create  bullet ai at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ufo.rect.midtop
        
        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
    
    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

class RocketBullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ss_game):
        """Create  bullet SS at the ship's current position."""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.color = self.settings.bullet_color
        
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midleft = ss_game.rocket.rect.midleft
        
        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)
    
    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.x -= self.settings.bullet_speed
        # Update the rect position
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)