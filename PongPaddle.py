from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector





class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball, speed_factor):
        if self.collide_widget(ball):
            vx,vy = ball.velocity

            offset = (ball.center_y - self.center_y) / (self.height / 2)

            bounced = Vector(-1 * vx, vy)

            vel = bounced * speed_factor

            ball.velocity = vel.x, vel.y + offset