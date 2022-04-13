import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/ufo.bmp')
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect =  self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
    
    def update(self):
        """Move the alien to the right"""
        self.x += (self.settings.alien_speed * 
                        self.settings.fleet_direction)
        self.rect.x = self.x

class SidewayAlien(Sprite):
    """A class to represent a single alien in the fleet."""
    def __init__(self, ss_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/ufo.bmp')
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect =  self.image.get_rect()
        self.rect.topright = ((1280 - self.rect.width), 
                                (720 - self.rect.height))
    
    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.top >= screen_rect.top or self.rect.bottom <= 0:
            return True
    
    def update(self):
        """Move the alien to the top or bottom."""
        self.rect.top -= (self.settings.alien_speed *
                            self.settings.fleet_direction)

        # Store the alien's exact vertical position.
        self.x = float(self.rect.top)