from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from PongBall import PongBall
from PongPaddle import PongPaddle
from kivy.core.window import Window

class ponggame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    # constructor
    def __init__(self, **kwargs):
        super(ponggame, self).__init__(**kwargs)
        
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel
    
    def update(self, dt):
        self.ball.move()

        # bounce ball off paddles
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        #bounce off top/bottom
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        # fell to score point
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4, 0))
        if self.ball.x > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0))

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.center_y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if (keycode[1] == "w"):
            self.player1.center_y += 30

        elif (keycode[1] == "s"):
            self.player1.center_y -= 30

        elif (keycode[1] == "up"):
            self.player2.center_y += 30

        elif (keycode[1] == "down"):
            self.player2.center_y -= 30

        return True