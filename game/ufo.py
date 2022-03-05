import pygame

class Ufo:

    def __init__(self, ai_game):
        """"Initialize the UFO and set its staring position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the UFO image and get its rect.
        self.image = pygame.image.load('images/ufo.bmp')
        self.rect = self.image.get_rect()

        # Start each new UFO at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """Draw the UFO at its current location"""
        self.screen.blit(self.image, self.rect)