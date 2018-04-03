from gameobject import GameObject
from area import Area
from generator import *
from character import Character
import tdl

class Game:
    def __init__(self):
        self.SCREEN_WIDTH = 110
        self.SCREEN_HEIGHT = 60
        self.LIMIT_FPS = 20
        tdl.set_font('arial12x12.png', greyscale = True, altLayout = True)
        self.FOV_ALGO = 'Basic'
        self.PANEL_HEIGHT = 12
        self.BAR_WIDTH = 20
        self.PANEL_Y = self.SCREEN_HEIGHT-self.PANEL_HEIGHT
        self.MSG_X = 2
        self.MSG_WIDTH = 30
        self.MSG_HEIGHT = self.PANEL_HEIGHT - 5

        self.MOVEMENT_KEYS = {
            'UP': [0,-1],
            'DOWN':[0,1],
            'LEFT':[-1,0],
            'RIGHT':[1,0],
            'KP1':[-1, 1],
            'KP2':[ 0, 1],
            'KP3':[ 1, 1],
            'KP4':[-1, 0],
            'KP6':[ 1, 0],
            'KP7':[-1,-1],
            'KP8':[ 0,-1],
            'KP9':[ 1,-1]
            }
        self.ACTION_KEYS = {
            'J' : 'jump',
            'j' : 'jump',
            'D' : 'debug',
            'd' : 'debug',
            'M' : 'menu',
            'm' : 'menu',
            'w' : 'where',
            'W' : 'where'
            }
# Y is down, X is Right
        self.CENTERX = self.SCREEN_WIDTH//2
        self.CENTERY = self.SCREEN_HEIGHT//2
        self.console = tdl.Console(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.main_window = tdl.init(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, title="Neolithic Rogue", fullscreen = False)
        self.fov_recompute = True
        self.game_state = 'playing'
        self.currentArea = None
        self.player = Character('@', (255,0,255), self.CENTERX, self.CENTERY, 'Player')

    def render_game(self):
        self.currentArea.draw(self.console, self.player.x-self.CENTERX, self.player.y-self.CENTERY, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.main_window.blit(self.console, 0, 0, self.SCREEN_WIDTH, self.SCREEN_HEIGHT, 0, 0)
        tdl.flush()
        for drawx in range(0, self.SCREEN_WIDTH):
                for drawy in range(0, self.SCREEN_HEIGHT):
                    self.console.draw_char(drawx, drawy, ' ', bg=self.currentArea.floorColor)

    def game_loop(self):
        while not tdl.event.is_window_closed():
            if self.game_state == 'playing':
                self.render_game()
                for event in tdl.event.get():
                    if event.type == 'KEYDOWN' and event.keychar != 'TEXT' and self.game_state == 'playing':
                        key_x, key_y = self.MOVEMENT_KEYS.get(event.keychar, (0,0))
                        action = self.ACTION_KEYS.get(event.keychar, (0,0))
                        self.player.move(self.currentArea, key_x, key_y)



main_game = Game();
initialArea = Area(0,0, 500, 500, 'savannah', 'Sav 0,0', (204, 255, 51))
main_game.currentArea = initialArea
main_game.currentArea.animalList.append(main_game.player)
newGenerator = SavannahGenerator()
newGenerator.generate(main_game.currentArea)
main_game.game_loop()
