from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from PongBall import PongBall
from PongPaddle import PongPaddle
from kivy.core.window import Window
import logging
from kivy.clock import Clock
from kivy.uix.label import Label


class ponggame(Widget):

    paddle_speed = 20

    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    winner_label = Label()

    # constructor
    def __init__(self, **kwargs):
        super(ponggame, self).__init__(**kwargs)

        self.winner_label.font_size = 70
        self.winner_label.center_x = self.width/2
        self.winner_label.top = self.top - 50
        self.winner_label.texture
        # self.winner_label.text = "Hi, EPIC MAN"

        Clock.schedule_interval(self.increase_ball_speed, 60)

        self.pressed_keys = set()

        self.pressed_actions = {
            "w": lambda: self.move_paddle_upward("w"),
            "up": lambda: self.move_paddle_upward("up"),
            "s": lambda: self.move_paddle_downward("s"),
            "down": lambda: self.move_paddle_downward("down")

        }
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)

        self._keyboard.bind(on_key_down=self._on_keyboard_down)

        self._keyboard.bind(on_key_up=self._on_keyboard_up)

    def increase_ball_speed(self, dt):

        logging.info(
            "In ponggame - increase_ball_speed(), speed factor: " + str(self.ball.speed_factor))

        self.ball.speed_factor += .0005

    def move_paddle_upward(self, keycode):
        if(keycode == "w"):
            if(self.player1.center_y + self.paddle_speed < self.height):
                self.player1.center_y += self.paddle_speed

        elif(keycode == "up"):
            if(self.player2.center_y + self.paddle_speed < self.height):
                self.player2.center_y += self.paddle_speed

    def _on_keyboard_up(self, keyboard, keycode):
        self.pressed_keys.remove(keycode[1])

    def move_paddle_downward(self, keycode):
        logging.info(
            "In ponggame - move_paddle_downward(), key code: " + keycode)

        if(keycode == "down"):
            logging.info("In ponggame - move_paddle_downward(), key code: " + keycode +
                         ".  player 2 y position:" + str(self.player2.center_y - self.paddle_speed))

            if(self.player2.center_y - self.paddle_speed > 0):
                self.player2.center_y -= self.paddle_speed
        elif(keycode == "s"):
            if(self.player1.center_y - self.paddle_speed > 0):
                self.player1.center_y -= self.paddle_speed

    def serve_ball(self, vel=(4, 0)):
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
            self.player1.center_y = touch.center_y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)

        self._keyboard.unbind(on_key_up=self._on_keyboard_up)
        self._keyboard = None
        # self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        # self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        self.pressed_keys.add(keycode[1])

        logging.info(
            "In ponggame - _on_keyboard_down(), screen height: " + str(self.height))

        return True
