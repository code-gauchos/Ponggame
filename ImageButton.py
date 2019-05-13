from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image


class ImageButton(ButtonBehavior, Image):
    def on_pressed(self):
        print("ImageButton - on_pressed(),")