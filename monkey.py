import arcade
import arcade.key

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class MonkeyGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        
        arcade.set_background_color(arcade.color.LIME)
        
        #self.monkey_sprite = ModelSprite('images/monkey.png',model=self.world.monkey)
        #self.banana_sprite = ModelSprite('images/banana.png',model=self.world.banana)
        #self.bomb_sprite = ModelSprite('images/bomb.png',model=self.world.bomb)
    
    def on_draw(self):
        arcade.start_render()
        #self.monkey_sprite.draw()
        #self.banana_sprite.draw()
        #self.bomb_sprite.draw()

        #arcade.draw_text(str(self.world.score),
        #                 self.width - 30, self.height - 30,
        #                 arcade.color.WHITE, 20)

    #def update(self, delta):
    #    self.world.update(delta)
        
    #def on_key_press(self, key, key_modifiers):
    #    self.world.on_key_press(key, key_modifiers)

if __name__ == '__main__':
    window = MonkeyGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()