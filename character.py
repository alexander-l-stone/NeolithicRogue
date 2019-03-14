from .gameobject import GameObject
from .actionmanager import *

class Character(GameObject):
    def __init__(self, char, color, x, y, name, visionBlock=False, moveBlock=False, bgcolor=None):
        GameObject.__init__(self, char, color, x, y, visionBlock=False, moveBlock=False, bgcolor=None)

    def move(self, area, dx, dy):
        if (attemptMove(self, area, dx, dy)):
            print("Im successfully moving")
            self.x += dx
            self.y += dy
