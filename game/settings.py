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

        # UFO settings
        self.ufo_speed = 2

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 204)
        self.bullets_allowed = 3
