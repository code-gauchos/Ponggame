from kivy.app import App
from ponggame import ponggame
from kivy.clock import Clock





# this was "pongapp"
class PongApp(App):
    def build(self):
        game = ponggame()
        game.serve_ball()

        # start game loop
        Clock.schedule_interval(game.update, 1.0 / 60.0)

        return game