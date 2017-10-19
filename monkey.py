import arcade
from models import Monkey,Basket

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

class MonkeyWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Monkey Keeper")
        self.background = arcade.load_texture("images/bgzoo.jpg")  
        self.Basket = Basket("images/basket.png",0.75)
        self.Monkey = Monkey("images/monkey.png", 0.5, self.Basket)
        self.score_text = arcade.create_text("Score : "+str(self.Monkey.score), arcade.color.BLACK, 30)
        self.game_over = arcade.create_text("GAME OVER", arcade.color.BLACK, 50)
    
    def on_key_release(self, key, modifiers):
        self.Basket.on_key_release(key, modifiers)
    
    def on_key_press(self, key, modifiers):
        self.Basket.on_key_press(key, modifiers)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.Monkey.on_draw()
        self.Basket.draw()
        if self.Monkey.score < 0 :
            arcade.render_text(self.game_over, 200, 300)
        else :
            arcade.render_text(self.score_text, 285, 300)

    def update(self, delta):
        self.Monkey.update()
        self.Basket.update()
        if self.Monkey.score < 0 :
            self.game_over = arcade.create_text("GAME OVER", arcade.color.BLACK, 50)
        else :
            self.score_text = arcade.create_text("Score : "+str(self.Monkey.score), arcade.color.BLACK, 30)

def main():
    window = MonkeyWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()