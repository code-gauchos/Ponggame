from kivy.uix.colorpicker import ColorWheel


class PongColorWheel(ColorWheel):
    
    def __init__(self, **kwargs):
        super(PongColorWheel, self).__init__(**kwargs)

        self.init_wheel(dt=0)

        def on__hsv(self, instance, value):

            

            super(PongColorWheel, self).on__hsv(instance, value)

            print("In PongColorWheel - on__hsv(), color selected: " + str (self.rgba))