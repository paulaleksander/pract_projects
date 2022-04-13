import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import AiScoreboard
from button import AiButton
from ship import Ship
from ufo import Ufo 
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # Make the Play button.
        self.play_button = AiButton(self, "Play")

        # Create an instance to store game statistics.
        #   and create a scoreboard.
        self.stats = GameStats(self)
        self.sb = AiScoreboard(self)

        self.ship = Ship(self)
        self.ufo = Ufo(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
                
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self.ufo.update()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    
    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game settings.
            self.settings.initialize_dynamic_settings()
            # Reset the game statistics.
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            pygame.mouse.set_visible(False)

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ufo.
            self._create_fleet()
            self.ufo.center_ufo()
    
    def _check_keydown_events(self, event):
        """Respond keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ufo.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ufo.moving_left = True
        elif event.key == pygame.K_UP:
            self.ufo.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ufo.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key ==pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ufo.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ufo.moving_left = False
        elif event.key == pygame.K_UP:
            self.ufo.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ufo.moving_down = False
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
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
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        
        if not self.aliens:
                # Destroy existing bullets and create new fleet.
                self.bullets.empty()
                self._create_fleet()
                self.settings.increase_speed()

                # Increase level
                self.stats.level += 1
                self.sb.prep_level()
        
    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_alien_x = available_space_x // (2 * alien_width)
        
        # Determine the number of rows of aliens that fit in the screen.
        ufo_height = self.ufo.rect.height
        available_space_y = (self.settings.screen_height - 
                                (3 * alien_height) - ufo_height)
        number_rows = available_space_y // (4 * alien_height)

        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_alien_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in rhe row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _ufo_hit(self):
        """Respond to the ufo being hit by an alien."""
        if self.stats.ufo_left > 0:

            # Decrement ufo_left.
            self.stats.ufo_left -= 1

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ufo.
            self._create_fleet()
            self.ufo.center_ufo()

            # Pause.
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
        
    def _check_fleet_edges(self):
        """respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            self._change_fleet_directions()
            break

    def _change_fleet_directions(self):
        """Drop the entire fleet and change the fleet direcrions."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Theat this the same as if the ship got hit.
                self._ufo_hit()
                break
    
    def _update_aliens(self):
        """
        Check if the fleet is at an edge,
         then update the position of all aliens in the fleet.
        """
        self._check_fleet_edges()
        self.aliens.update()

        # Look for aliens-ufo collisions.
        if pygame.sprite.spritecollideany(self.ufo, self.aliens):
            self._ufo_hit()
        
        # Looks for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()
            
    def _update_screen(self):
        """Update image in the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ufo.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Draw the score information.
        self.sb.show_score()

        # Draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()
        
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()