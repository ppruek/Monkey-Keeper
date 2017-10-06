import arcade
from models import Monkey

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

class MonkeyWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Monkey Keeper")
        self.background = arcade.load_texture("images/bgzoo.jpg")  
        self.Monkey = Monkey("images/monkey.png", 0.5)
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.Monkey.draw()

    def update(self, delta):
        self.Monkey.update()

def main():
    window = MonkeyWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()