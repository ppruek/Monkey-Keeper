import arcade
from models import World,Monkey
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

class MonkeyWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.background = arcade.load_texture("images/bgzoo.jpg")
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.monkey_sprite = arcade.Sprite("images/monkey.png", 0.5)
        self.monkey_sprite.center_x = SCREEN_WIDTH // 2
        self.monkey_sprite.center_y = SCREEN_HEIGHT - 70

    def update(self, delta):
        self.world.update(delta)
 
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.monkey_sprite.draw()
    
class MonkeySprite:
    def __init__(self, monkey):
        self.monkey = monkey
        
def main():
    window = MonkeyWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()