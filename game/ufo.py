import pygame

class Ufo:

    def __init__(self, ai_game):
        """"Initialize the UFO and set its staring position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the UFO image and get its rect.
        self.image = pygame.image.load('images/ufo.bmp')
        self.rect = self.image.get_rect()

        # Start each new UFO at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Store a decimal value for the UFO's horizontal and vertical positions.
        self.x = int(self.rect.x)
        self.y = int(self.rect.y)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Update the UFO's position based in the movement flags."""
        # Update the UFO's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ufo_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ufo_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ufo_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ufo_speed
        
        # Update rect obj from self.x and self.y
        self.rect.x = self.x
        self.rect.y = self.y
    
    def blitme(self):
        """Draw the UFO at its current location"""
        self.screen.blit(self.image, self.rect)

class SidewayUfo:

    def __init__(self, ai_game):
        """"Initialize the UFO and set its staring position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the UFO image and get its rect.
        self.image = pygame.image.load('images/ufo.bmp')
        self.rect = self.image.get_rect()

        # Start each new UFO at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Store a decimal value for the UFO's horizontal and vertical positions.
        self.x = int(self.rect.x)
        self.y = int(self.rect.y)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Update the UFO's position based in the movement flags."""
        # Update the UFO's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ufo_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ufo_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ufo_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ufo_speed
        
        # Update rect obj from self.x and self.y
        self.rect.x = self.x
        self.rect.y = self.y
    
    def blitme(self):
        """Draw the UFO at its current location"""
        self.screen.blit(self.image, self.rect)