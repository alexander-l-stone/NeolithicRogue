from gameobject import GameObject
from area import Area
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

    def render_game(self):
        self.currentArea.draw(self.console, 0, 0, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.main_window.blit(self.console, 0, 0, self.SCREEN_WIDTH, self.SCREEN_HEIGHT, 0, 0)
        tdl.flush()
        self.currentArea.clear(self.console, -self.CENTERX, -self.CENTERY, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

    def game_loop(self):
        while not tdl.event.is_window_closed():
            if self.game_state == 'playing':
                self.render_game()



main_game = Game();
initialArea = Area(0,0, 200, 200, 'savannah', 'Sav 0,0', (204, 255, 51))
tree = GameObject('T', (0, 102, 0), 32, 32)
initialArea.objList.append(tree)
main_game.currentArea = initialArea
main_game.game_loop()