#Random generation functions go here
from gameobject import GameObject
from random import *
#TODO: Add seed to RNG
#tree GameObject('T', (0, 102, 0), 32, 32)

class SavannahGenerator:
    def __init__(self):
        self.seed = 0

    def generateTrees(self, area):
        numPatches = randrange(0, 50)
        for patch in range(numPatches):
            randx = randrange(area.x-area.width//2+10, area.x+area.width//2-10)
            randy = randrange(area.y-area.height//2+10, area.y+area.height//2-10)
            numTrees = randrange(0, 150)
            for tree in range(numTrees):
                randTreeX = randrange(randx-10, randx+10)
                randTreeY = randrange(randy-10, randy+10)
                foundCollision = False
                for obj in area.objList:
                    if obj.x == randTreeX and obj.y == randTreeY:
                        foundCollision = True
                        break
                if not foundCollision:
                    newTree = GameObject('T', (0, 102, 0), randTreeX, randTreeY)
                    area.objList.append(newTree)
