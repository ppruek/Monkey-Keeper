import arcade
import arcade.key

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

class Monkey(arcade.Sprite):
    def __init__(self, link,size):
        super().__init__(link,size)
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = SCREEN_HEIGHT - 70
        self.speed = 3
        
    def movement(self):
        if self.center_x > 660 or self.center_x < 20:
            self.speed *= -1
        self.center_x += self.speed
        
    def update(self):
        self.movement()
        super().draw() 

class Basket(arcade.Sprite):
    def __init__(self, link, size):
        super().__init__(link, size)
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = 50
        self.change_x = 0

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.change_x = -5
        if key == arcade.key.RIGHT:
            self.change_x = 5
    
    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
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

class Banana(arcade.Sprite):
    def __init__(self, link, size, Monkey, Basket):
        super().__init__(link,size)
        self.Monkey = Monkey
        self.Basket = Basket
        self.center_x = Monkey.center_x
        self.center_y = Monkey.center_y
    
    def movement(self):
        self.center_y -= 1
    
    def update(self):
        self.movement()
        super().draw()

    #def is_hit(self):
