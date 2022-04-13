import sys
from time import sleep
import pygame
from settings import SidewayShooterSettings
from ss_game_stats import GameStats
from scoreboard import SsScoreboard
from button import SsButton
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

        # Create an instance to store game statistics.
        #   and create a scoreboard.
        self.stats = GameStats(self)
        self.sb = SsScoreboard(self)

        # Make the Play button.
        self.play_button = SsButton(self, "Play")
        
        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()
                
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
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

            # Create a new fleet and center the rocket.
            self._create_fleet()
            self.rocket.center_rocket()
    
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
        alien = SidewayAlien(self)
        alien_width, alien_height = alien.rect.size
        availible_space_y = self.settings.screen_height - (2 * alien_width)
        number_aliens_y = availible_space_y // (2 * alien_width)

        # Determine the number of rows of aliens that fir on the screen.
        rocket_height = self.rocket.rect.height
        availible_space_x = (self.settings.screen_width - 
                                (3 * alien_height) - rocket_height)
        number_rows = availible_space_x // (4 * alien_height)

        # Create full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_y):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
            # Create an alien and place it in the row
            alien = SidewayAlien(self)
            alien_width, alien_height = alien.rect.size
            alien.y = alien_width + 2 * alien_width * alien_number
            alien.rect.y = alien.y
            alien.x = alien_height + 2 * alien_height * row_number
            alien.rect.x = alien.x
            alien.rect.topright = ((1280 - alien.x), (720 - alien.y))

            self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's directions."""
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _rocket_hit(self):
        """Respond to the rocket hit by an alien."""
        if self.stats.rocket_left > 0:
            # Decrement rocket left.
            self.stats.rocket_left -= 1

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the rocket.
            self._create_fleet()
            self.rocket.center_rocket()

            # Pause.
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(False)
    
    def _check_aliens_left(self):
        """Check if any aliens have reached the left of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.top >= screen_rect.left:
                # Treat this the same as if the ship got hit.
                self._rocket_hit
                break
    
    def _update_aliens(self):
        """
        Check if the fleet is at an edge,
            then update the positions of all aliens in the fleet.."""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-rocket collisions.
        if pygame.sprite.spritecollideany(self.rocket, self.aliens):
            self._rocket_hit()
        
        # Look for aliens hitting the left of the screen.
        self._check_aliens_left()
    
    def _update_screen(self):
        """Update image in the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
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
    ss = SidewayShooter()
    ss.run_game()