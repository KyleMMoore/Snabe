class Settings():
    """Snabe settings and constants"""

    def __init__(self):
        """Init the game settings"""
        # screen settings
        self.screen_width = 800
        self.screen_height = 800
        self.background_color = (255, 255, 255)
        self.base_speed = 1
        self.tick_rate = 60
        self.game_length = 60