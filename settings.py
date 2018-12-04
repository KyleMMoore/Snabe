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

        #constants for calculating game speed/time
        self.tick_rate = 60
        self.game_length = 60

        #constants to determine spawn rates (per n seconds)
        self.food_spawn_rate = 5
        self.wafer_spawn_rate = 15

        #Stores the active food and wafer objects
        self.food_list = []
        self.wafer_list = []

        #TODO: store entities and rects here instead of passing them to everything
        self.entities = []
        self.entities_rects = []

