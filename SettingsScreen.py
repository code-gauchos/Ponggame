from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.screenmanager import Screen
from PongColorWheel import PongColorWheel









class SettingsScreen(Screen):

    player_1_name_widget = ObjectProperty(None)

    player_1_paddle_color = ObjectProperty(None)
    player_1_label_color = ListProperty([0, 0, 0, 1])


    def save(self):


        self.manager.get_screen("game_screen").player_1_name = self.player_1_name_widget.text
            
        

        self.manager.current = "game_screen"


    def player_1_paddle_on_color(self, rgba_color):
        print("In SettingsScreen - player_1_paddle_on_color(), RGBA =", str(rgba_color))

        self.player_1_label_color = rgba_color

        self.manager.get_screen("game_screen").player_1_paddle_color = rgba_color

       