class GameStats:
    """Track statictics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statictics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # Start Alien invasion in an active state
        self.game_active = True

    def reset_stats(self):
        """initialize statistics that can change during the game."""
        self.ufo_left = self.settings.ufo_limit
