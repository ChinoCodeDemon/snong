import pyglet
from pyglet import shapes
from objects.collideable import Collideable

player_speed = 300

class PaddleKeyhandler:
    y_velocity = 0
    def __init__(self, up, down) -> None:
        self.up = up
        self.down = down
    def handle_key_press(self, keyval):
        if keyval == self.up:
            self.y_velocity += player_speed
        if keyval == self.down:
            self.y_velocity -= player_speed
    def handle_key_release(self, keyval):
        if keyval == self.up:
            self.y_velocity -= player_speed
        if keyval == self.down:
            self.y_velocity += player_speed

class Paddle(PaddleKeyhandler, Collideable):
    width: int
    height: int

    def __init__(self, width, height, up, down) -> None:
        super().__init__(up, down)
        self.width = width
        self.height = height

    def set_startpos(self, window: pyglet.window.Window, batch, left: bool):
        ypos = window.height * .5 - self.height * .5
        if left:
            self.bounding = shapes.Rectangle(0, ypos, self.width, self.height, batch=batch)
        else:
            self.bounding = shapes.Rectangle(window.width - self.width, ypos, self.width, self.height, batch=batch)

    def update(self, dt: float, window: pyglet.window.Window):
        self.bounding.y += self.y_velocity * dt
        if self.bounding.y < 0:
            self.bounding.y = 0
        if self.bounding.y + self.bounding.height > window.height:
            self.bounding.y = window.height - self.bounding.height