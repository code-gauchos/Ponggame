from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ListProperty
from kivy.vector import Vector

class PongBall(Widget):
    
    color = ListProperty([1, 1, 1, 1])


    speed_factor = 1.1
   
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
        