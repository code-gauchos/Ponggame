from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, ListProperty



class GameScreen(Screen):
    # player_1_name = lili
    player_1_name = "Player 1"
    player_1_paddle_color = ListProperty(None)
    
    
    game_engine=ObjectProperty(None)

    def on_pre_enter(self):

        self.game_engine.player_1_name = self.player_1_name
        
        self.game_engine.player1.color = self.player_1_paddle_color
        self.game_engine.player_1_color = self.player_1_paddle_color
        
        
        
        
        # when screen comes into view, start the game
        self.game_engine.start()


