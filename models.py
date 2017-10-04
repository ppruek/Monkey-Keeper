import arcade.key
from random import randint

class Monkey:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

    def update(self, delta):
        self.x = 0
        self.y = 0
        
class Basket:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

    def update(self, delta):
        self.x = 0
        self.y = 0

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.monkey = Monkey(self, width // 2, height // 2)

    def update(self, delta):
        self.monkey.update(delta)
