import pygame

class Rocket:

    def __init__(self, ss_game):
        """"Initialize the rocket and set its staring position."""
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.screen_rect = ss_game.screen.get_rect()

        # Load the rocket image and get its rect.
        self.image = pygame.image.load('images/rocket.bmp')
        self.rotated_image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()

        # Start each new rocket at the left center of the screen.
        self.rect.midleft = self.screen_rect.midleft
        
        # Store a decimal value for the rocket's horizontal and vertical positions.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Update the rocket's position based in the movement flags."""
        # Update the rocket's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        
        # Update rect obj from self.x and self.y
        self.rect.x = self.x
        self.rect.y = self.y
    
    def blitme(self):
        """Draw the rocket at its current location"""
        self.screen.blit(self.rotated_image, self.rect)