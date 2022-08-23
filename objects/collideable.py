from __future__ import annotations
from pyglet import shapes

class Collideable:
    bounding: shapes.Rectangle
    def does_collide(self, other: Collideable) -> bool:
        if self.bounding.x > other.bounding.x + other.bounding.width:
            return False
        if other.bounding.x > self.bounding.x + self.bounding.width:
            return False
        if self.bounding.y > other.bounding.y + other.bounding.height:
            return False
        if other.bounding.y > self.bounding.y + self.bounding.height:
            return False
        return True
    
    def get_center(self):
        return (
            self.bounding.x + self.bounding.width * 0.5,
            self.bounding.y + self.bounding.height * 0.5
            )