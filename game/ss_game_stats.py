class GameStats:
    """Track statictics for Sideway Shooter."""

    def __init__(self, ss_game):
        """Initialize statictics."""
        self.settings = ss_game.settings
        self.reset_stats()
        # Start Sideway Shooter in an active state
        self.game_active = False

    def reset_stats(self):
        """initialize statistics that can change during the game."""
        self.rocket_left = self.settings.rocket_limit
