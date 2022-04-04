import sys
import pygame
from settings import SidewayShooterSettings
from rocket import Rocket
from bullet import RocketBullet
from alien import SidewayAlien

class SidewayShooter:
    
    def __init__(self):
        pygame.init()
        self.settings = SidewayShooterSettings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Sideway Shooter")

        # Set the background color.
        self.bg_color = (230, 230, 230)
        
        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
                
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.rocket.update()
            self._update_bullets()
            self._update_aliens()         
            self._update_screen()        
            
            # Make the most recently drawn screen visible.
            pygame.display.flip()
    
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """Respond keypresses."""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key ==pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = RocketBullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of bullets."""
        # Get rid of bullets that have disappeared.
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()
    
    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)
        
        if not self.aliens:
                # Destroy existing bullets and create new fleet.
                self.bullets.empty()
                self._create_fleet()
        
    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width
        alien = SidewayAlien(self)
        alien_width, alien_height = alien.rect.size
        available_space_y = self.settings.screen_height - (2 * alien_height)
        number_alien_y = available_space_y // (2 * alien_height)
        
        # Determine the number of rows of aliens that fit in the screen.
        rocket_width = self.rocket.rect.width
        available_space_x = (self.settings.screen_width - 
                                (2 * alien_width) - rocket_width)
        number_rows = available_space_x // (4 * alien_width)

        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_alien_y):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in rhe row"""
        alien = SidewayAlien(self)
        alien_width, alien_height = alien.rect.size
        alien.y = alien_width + 2 * alien_width * alien_number
        alien.rect.y = alien.y
        alien.rect.x = alien_height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_screen(self):
        """Update image in the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
    
    def _check_fleet_edges(self):
        """respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            self._change_fleet_directions()
            break

    def _change_fleet_directions(self):
        """Drop the entire fleet and change the fleet direcrions."""
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def _update_aliens(self):
        """
        Check if the fleet is at an edge,
         then update the position of all aliens in the fleet.
        """
        self._check_fleet_edges()
        self.aliens.update()
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ss = SidewayShooter()
    ss.run_game()