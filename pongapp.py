from kivy.app import App
from ponggame import PongGame
from kivy.clock import Clock
from WelcomeScreen import WelcomeScreen
from kivy.uix.screenmanager import ScreenManager
from GameScreen import GameScreen
from SettingsScreen import SettingsScreen






# this was "pongapp"
class PongApp(App):
    def build(self):
       
        PongApp.pong_screen_manager = ScreenManager()

        welcome_screen = WelcomeScreen(name="welcome_screen")
        game_screen = GameScreen(name="game_screen")
        settings_screen = SettingsScreen(name="settings_screen")


        self.pong_screen_manager.add_widget(welcome_screen)
        self.pong_screen_manager.add_widget(game_screen)
        self.pong_screen_manager.add_widget(settings_screen)
        
        # return game
        return self.pong_screen_manager

