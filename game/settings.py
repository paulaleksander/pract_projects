class Settings:
    """A class to store all setiings for Alien Invasion."""

    def __init__(self):
        """Initialise the game's static settings"""
        # Screen settings
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (0, 0, 139)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # UFO settings
        self.ufo_speed = 2
        self.ufo_limit = 3

        # Bullet settings
        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 204)
        self.bullets_allowed = 25

        # Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 1.0
        # fleet_directions of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien points values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Initialize settings that changes throughout the game."""
        self.ufo_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # Fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Incerease speed settings and alien point values."""
        self.ufo_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

class SidewayShooterSettings:
    """A class to store all setings for Sideway Shooter."""

    def __init__(self):
        """Initialise the game's static settings"""
        # Screen settings
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (99,102,106)
         
        # rocket settings
        self.rocket_speed = 2.5
        self.rocket_limit = 3

        # Bullet settings
        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (152, 251, 152)
        self.bullets_allowed = 25

        # Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 1.0
        # fleet_directions of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien points values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Initialize settings that changes throughout the game."""
        self.rocket_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # Fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Incerease speed settings and alien point values."""
        self.rocket_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)