import arcade
import arcade.key
from random import randint

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

class Banana(arcade.Sprite):
    def __init__(self, x, y, speed):
        super().__init__("images/bananas.png",0.5)
        self.center_x = x
        self.center_y = y
        self.speed = speed

    def update(self):
        self.center_y -= self.speed

class Bomb(arcade.Sprite):
    def __init__(self, x, y, speed):
        super().__init__("images/bomb.png",1)
        self.center_x = x
        self.center_y = y
        self.speed = speed

    def update(self):
        self.center_y -= self.speed        

class Monkey(arcade.Sprite):
    def __init__(self, link,size):
        super().__init__(link,size)
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = SCREEN_HEIGHT - 70
        self.speed = 3
        self.Banana = []
        self.Bomb = []

    def movement(self):
        if self.center_x > 660 or self.center_x < 20:
            self.speed *= -1
        self.center_x += self.speed

    def create(self):
        time = randint(0,1000000) 
        if time > 975000:
            self.Banana.append(Banana(self.center_x,self.center_y,3)) 
        if time > 990000:
            self.Bomb.append(Bomb(self.center_x,self.center_y,2))

    def update(self):
        self.movement()     
        self.create()
        for Banana in self.Banana:
            if Banana.center_y < 0:
                self.Banana.remove(Banana)
            Banana.update()
        for Bomb in self.Bomb:
            if Bomb.center_y < 0:
                self.Bomb.remove(Bomb)
            Bomb.update()
      
    def on_draw(self):
        super().draw()
        for Banana in self.Banana:
            Banana.draw()
        for Bomb in self.Bomb:
            Bomb.draw()
        
class Basket(arcade.Sprite):
    def __init__(self, link, size):
        super().__init__(link, size)
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = 50
        self.change_x = 0
        self.direc = True

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.change_x = -5
            self.direc = False
        if key == arcade.key.RIGHT:
            self.change_x = 5
            self.direc = True
        if key == arcade.key.SPACE:
            if self.direc :
                self.change_x = 8
            else :
                self.change_x = -8
    
    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT or key == arcade.key.SPACE:
            self.change_x = 0
    
    def is_end(self):
        if self.center_x > 680 :
            self.center_x = 680
        elif self.center_x < 20 :
            self.center_x = 20

    def update(self):
        super().draw()
        self.is_end()
        self.center_x += self.change_x           

