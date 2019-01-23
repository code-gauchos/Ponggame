from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty



class GameScreen(Screen):
    # player_1_name = lili
    game_engine=ObjectProperty(None)

    def on_enter(self):

        # when screen comes into view, start the game
        self.game_engine.start()

