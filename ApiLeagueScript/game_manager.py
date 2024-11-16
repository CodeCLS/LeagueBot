class game_manager:
    def __init__(self):
        self.game_instance = None
    def get_game_data(self):
        real_time = RiotRealTimeGameApi()