import arcade.key
import arcade
from random import randint

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

class Monkey(arcade.Sprite):
    def __init__(self, link,size):
        super().__init__(link,size)
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = SCREEN_HEIGHT - 70
        self.speed = 3
        
    def movement(self):
        if self.center_x > 700 or self.center_x < 0:
            self.speed *= -1
        self.center_x += self.speed
        
    def update(self):
        self.movement()
        super().draw()        