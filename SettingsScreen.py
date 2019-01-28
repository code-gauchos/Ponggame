from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.screenmanager import Screen









class SettingsScreen(Screen):

    player_1_name_widget = ObjectProperty(None)


    def save(self):


        self.manager.get_screen("game_screen").player_1_name = self.player_1_name_widget.text
            

        self.manager.current = "game_screen"   
       