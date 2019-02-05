from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, ListProperty





class GameScreen(Screen):
    # player_1_name = lili
    player_1_name = "Player 1"
    player_1_paddle_color = ListProperty(None)

    player_2_name = "Player 2"
    
    
    game_engine=ObjectProperty(None)

    def on_pre_enter(self):

        self.game_engine.player_1_name = self.player_1_name
        
        self.game_engine.player1.color = self.player_1_paddle_color
        self.game_engine.player_1_color = self.player_1_paddle_color

        self.game_engine.player_2_name = self.player_2_name
        
        
        
        
        # when screen comes into view, start the game
        self.game_engine.start()


