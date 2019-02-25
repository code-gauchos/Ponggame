from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from PongBall import PongBall
from PongPaddle import PongPaddle
from kivy.core.window import Window
import logging
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup


class PongGame(Widget):

    is_game_on = False
    paddle_speed = 20
    max_score = NumericProperty(11)
    player_1_name = StringProperty("Player 1")
    player_2_name = StringProperty("Player 2")
    esc_popup = Popup()


    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    winner_label = Label()

    # constructor
    def __init__(self, **kwargs):
        super(PongGame, self).__init__(**kwargs)

        self.initialize()

        # self.winner_label.font_size = 70
        # self.winner_label.center_x = self.width/2
        # self.winner_label.top = self.top - 50
        # self.winner_label.texture
        # # self.winner_label.text = "Hi, EPIC MAN"

        
        
    def initialize(self):
        self.is_game_on = True
        
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)

        self._keyboard.bind(on_key_down=self._on_keyboard_down)

        self._keyboard.bind(on_key_up=self._on_keyboard_up) 

        self.pressed_keys = set()

        self.pressed_actions = {
            "w": lambda: self.move_paddle_upward("w"),
            "up": lambda: self.move_paddle_upward("up"),
            "s": lambda: self.move_paddle_downward("s"),
            "down": lambda: self.move_paddle_downward("down")

        }

        self.set_popup()

        Clock.schedule_interval(self.increase_ball_speed, 60)

        


    def increase_ball_speed(self, dt):

        logging.info(
            "In ponggame - increase_ball_speed(), speed factor: " + str(self.ball.speed_factor))

        self.ball.speed_factor += .0005

    def move_paddle_upward(self, keycode):
        
        paddle_offset = 55
        
        if(keycode == "w"):
            if(self.player1.center_y + self.paddle_speed + paddle_offset < self.height):
                self.player1.center_y += self.paddle_speed

        elif(keycode == "up"):
            if(self.player2.center_y + self.paddle_speed + paddle_offset < self.height):
                self.player2.center_y += self.paddle_speed

    def _on_keyboard_up(self, keyboard, keycode):
        if(self.pressed_keys.__contains__(keycode[1])):
            self.pressed_keys.remove(keycode[1])

    def resume_game(self):
        self.is_game_on = True

        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def pause_game(self):
        self.is_game_on = False

        Clock.unschedule(self.update)
    
    def move_paddle_downward(self, keycode):
        
        paddle_offset = 55
        
        logging.info(
            "In ponggame - move_paddle_downward(), key code: " + keycode)

        if(keycode == "down"):
            logging.info("In ponggame - move_paddle_downward(), key code: " + keycode +
                         ".  player 2 y position:" + str(self.player2.center_y - self.paddle_speed))

            if(self.player2.center_y - paddle_offset - self.paddle_speed > 0):
                self.player2.center_y -= self.paddle_speed
        elif(keycode == "s"):
            if(self.player1.center_y - paddle_offset - self.paddle_speed > 0):
                self.player1.center_y -= self.paddle_speed

    def start(self):
        # self.player_1_name = GameScreen.player_1_name
        

        self.initialize()

        self.serve_ball()

        # start game loop
        self.resume_game()


    def serve_ball(self, vel=(6, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        """update the game - Playground."""
        for key in self.pressed_keys:
            try:

                self.pressed_actions[key]()
            except KeyError:
                logging.error("In ponggame - update(), System encountered a possible key error. " +
                              str(key) + ".  Player might be alt-tab to other screen.")

        self.ball.move()

        # bounce ball off paddles
        self.player1.bounce_ball(self.ball, self.ball.speed_factor, True)
        self.player2.bounce_ball(self.ball, self.ball.speed_factor, False)

        # bounce off top/bottom
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        self.check_scoring()

    def check_scoring(self):
        # fell to score point
        if self.ball.x < self.x:
            self.player2.score += 1

            self.reset_paddle_positions()

            if(self.player2.score > 6):
                self.winner_label.text = "Player 2 Wins!"

            self.serve_ball(vel=(4, 0))

        if self.ball.x > self.width:
            self.player1.score += 1

            self.reset_paddle_positions()

            if(self.player1.score > 6):
                self.winner_label.text = "Player 1 Wins!"

            self.serve_ball(vel=(-4, 0))

    def reset_paddle_positions(self):
        self.player1.center_y = self.center_y
        self.player2.center_y = self.center_y

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)

        self._keyboard.unbind(on_key_up=self._on_keyboard_up)
        self._keyboard = None
        # self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        # self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        
        if (keycode[1] != "escape"):
            self.pressed_keys.add(keycode[1])
        else:
            if(self.is_game_on is True):
                self.pause_game()
                self.open_popup()
            else:
                self.resume_game()
                

        logging.info(
            "In ponggame - _on_keyboard_down(), screen height: " + str(self.height))

        return True

    def set_popup(self):
        welcome_button = Button(text="Home Screen", color=(1, 1, 1, 1))

        settings_button = Button(text="Settings", color=(1, 1, 1, 1))

        popup_box_layout = BoxLayout()

        popup_box_layout.spacing = 10
        popup_box_layout.size_hint = (.5, .25)

        popup_box_layout.add_widget(welcome_button)
        popup_box_layout.add_widget(settings_button)

        self.esc_popup = Popup(
            title="Exit", 
            content=popup_box_layout, 
            size_hint=(.35, .25), 
            auto_dismiss=False
        )


    def open_popup(self, *args):
        self.esc_popup.open()

    def close_popup(self, *args):

        self.esc_popup.dismiss()
