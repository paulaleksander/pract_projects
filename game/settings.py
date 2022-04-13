class Settings:
    """A class to store all setiings for Alien Invasion."""

    def __init__(self) -> None:
        """Initialise the game's settings"""
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

class SidewayShooterSettings:
    """A class to store all setings for Sideway Shooter."""

    def __init__(self) -> None:
        """Initialise the game's settings"""
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