class Settings():
    """Snabe settings and constants"""

    def __init__(self):
        """Init the game settings"""
        # screen settings
        self.screen_width = 800
        self.screen_height = 800
        self.background_color = (255, 255, 255)

        #snabe speed
        #TODO: Fix algorithm(s) to work with dif speed
        #ideal speed seems to be 2-3
        self.base_speed = 1

        #constants for calculating game speed:time
        self.tick_rate = 60
        self.game_length = 60

        #constants to determine spawn rates (per n seconds)
        self.food_spawn_rate = 7
        self.wafer_spawn_rate = 2

        #constants to determine each power-up's active time
        self.sword_time = 8
        self.shield_time = 12

        #Stores the active food and wafer objects
        self.food_list = []
        self.wafer_list = []

        #stores remaining time in game session
        self.timer_value = self.game_length * self.tick_rate

        #TODO: store entities and rects here instead of passing them to everything
        self.entities = list()
        self.entities_rects = list()

        #calculations that regulate seconds:tick rate
        self.sword_time = self.sword_time * self.tick_rate
        self.shield_time = self.shield_time * self.tick_rate
