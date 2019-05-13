from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ListProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.core.audio import SoundLoader


class PongPaddle(Widget):
    color = ListProperty([1, 1, 1, 1,])
    score = NumericProperty(0)
    paddle_1_sound = SoundLoader.load("./sounds/player_1_sound_2.wav")
    paddle_2_sound = SoundLoader.load("./sounds/player_2_sound_2.wav")

    def bounce_ball(self, ball, speed_factor, is_player_1):
        if self.collide_widget(ball):
            vx, vy = ball.velocity

            offset = (ball.center_y - self.center_y) / (self.height / 2)

            bounced = Vector(-1 * vx, vy)

            vel = bounced * speed_factor

            ball.velocity = vel.x, vel.y + offset

            if(is_player_1 == True):
                self.paddle_1_sound.play()
            else:
                self.paddle_2_sound.play()