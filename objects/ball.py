from objects.collideable import Collideable
from pyglet.window import Window
from pyglet import shapes

class Ball(Collideable):
    x_velocity: float
    y_velocity: float

    def __init__(self, width, height, x_vel, y_vel) -> None:
        self.width = width
        self.height = height
        self.x_velocity = x_vel
        self.y_velocity = y_vel

    def create_bounding(self, window: Window, batch):
        self.bounding = shapes.Rectangle(
            window.width * 0.5 - self.width * 0.5,
            window.height * 0.5 - self.height *0.5,
            self.width, self.height, 
            (0, 255, 0),
            batch=batch
            )

    def reset_position(self, window: Window):
        self.bounding.x = window.width * 0.5 - self.width * 0.5
        self.bounding.y = window.height * 0.5 - self.height *0.5

    def update(self, dt, window: Window, paddles: list[Collideable]):
        self.bounding.x += self.x_velocity * dt
        self.bounding.y += self.y_velocity * dt
        if self.bounding.y < 0:
            self.bounding.y = 0
            self.y_velocity = abs(self.y_velocity)
        if self.bounding.y + self.bounding.height > window.height:
            self.bounding.y = window.height - self.bounding.height
            self.y_velocity = -abs(self.y_velocity)
        
        for p in paddles:
            if self.does_collide(p):
                if self.get_center() < p.get_center():
                    self.x_velocity = -abs(self.x_velocity)
                else:
                    self.x_velocity = +abs(self.x_velocity)