#Random generation functions go here
from gameobject import GameObject
from random import *
#TODO: Add seed to RNG
#tree GameObject('T', (0, 102, 0), 32, 32)

class SavannahGenerator:
    def __init__(self):
        self.seed = 0

    def generate(self, area):
        self.generateTrees(area)
        self.generateRocks(area)

    def generateTrees(self, area):
        numPatches = randrange(0, int(area.height*area.width*0.001))
        for patch in range(numPatches):
            randx = randrange(area.x-area.width//2+10, area.x+area.width//2-9)
            randy = randrange(area.y-area.height//2+10, area.y+area.height//2-9)
            numTrees = randrange(0, 81)
            for tree in range(numTrees):
                randTreeX = randrange(randx-10, randx+11)
                randTreeY = randrange(randy-10, randy+11)
                foundCollision = False
                if ((randTreeX, randTreeY) in area.objList.values()):
                    foundCollision = True;
                if not foundCollision:
                    newTree = GameObject('T', (0, 102, 0), randTreeX, randTreeY, moveBlock=True)
                    area.objList[(newTree.x, newTree.y)] = newTree

    def generateRocks(self, area):
        numRocks = randrange(0, int(area.height*area.width*0.005))
        for rock in range(numRocks):
            randx = randrange(area.x-area.width//2+2, area.x+area.width//2-2)
            randy = randrange(area.y-area.height//2+2, area.y+area.height//2-2)
            foundCollision = False
            if ((randx, randy) in area.objList.values()):
                foundCollision = True;
            if not foundCollision:
                typeOfRock = randrange(0,101)
                if typeOfRock > 90:
                    bigRock = GameObject('#', (102,51,0), randx, randy, visionBlock=True, moveBlock=True)
                    area.objList[(bigRock.x, bigRock.y)] = bigRock
                    for x in range(bigRock.x-1, bigRock.x+2):
                        for y in range(bigRock.y-1, bigRock.y+2):
                            foundCollision = False
                            if ((x, y) in area.objList.values()):
                                foundCollision = True;
                            if not foundCollision:
                                if randrange(0,101) > 35:
                                    smallRock = GameObject('o', (153, 102, 0), x, y, moveBlock=True)
                                    area.objList[(smallRock.x, smallRock.y)] = smallRock
                else:
                    smallRock = GameObject('o', (153, 102, 0), randx, randy, moveBlock=True)
                    area.objList[(smallRock.x, smallRock.y)] = smallRock
