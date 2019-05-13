from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from ImageButton import ImageButton


class WelcomeScreen(Screen):
    play_image_button = ObjectProperty(None)
    settings_image_button = ObjectProperty(None)