#Random generation functions go here
from .gameobject import GameObject
import random
from math import cos, sin
#TODO: Add seed to RNG
#tree GameObject('T', (0, 102, 0), 32, 32)

class AreaGenerator:
    def __init__(self):
        return

class SavannahGenerator(AreaGenerator):
    def __init__(self):
        AreaGenerator.__init__(self)

    def generate(self, area):
        random.seed(area.seed)
        self.generateWater(area)
        self.generateTrees(area)
        self.generateRocks(area)

    def generateTrees(self, area):
        numPatches = random.randrange(0, int(area.height*area.width*0.001))
        for patch in range(numPatches):
            randx = random.randrange(area.x-area.width//2+10, area.x+area.width//2-9)
            randy = random.randrange(area.y-area.height//2+10, area.y+area.height//2-9)
            numTrees = random.randrange(0, 81)
            for tree in range(numTrees):
                randTreeTheta = random.randrange(0,360)
                randTreeR = random.randrange(0,36)
                foundCollision = False
                randTreeX = int(randx + randTreeR * cos(randTreeTheta))
                randTreeY = int(randy + randTreeR * sin(randTreeTheta))
                if ((randTreeX, randTreeY) in area.objList.values()):
                    foundCollision = True
                if not foundCollision:
                    newTree = GameObject('T', (0, 102, 0), randTreeX, randTreeY, "Tree", moveBlock=True)
                    area.objList[(newTree.x, newTree.y)] = newTree

    def generateRocks(self, area):
        numRocks = random.randrange(0, int(area.height*area.width*0.005))
        for rock in range(numRocks):
            randx = random.randrange(area.x-area.width//2+2, area.x+area.width//2-2)
            randy = random.randrange(area.y-area.height//2+2, area.y+area.height//2-2)
            foundCollision = False
            if ((randx, randy) in area.objList.values()):
                foundCollision = True
            if not foundCollision:
                typeOfRock = random.randrange(0,101)
                if typeOfRock > 60:
                    bigRock = GameObject('#', (102,51,0), randx, randy, 'Big-Rock', visionBlock=True, moveBlock=True)
                    area.objList[(bigRock.x, bigRock.y)] = bigRock
                    for x in range(bigRock.x-1, bigRock.x+2):
                        for y in range(bigRock.y-1, bigRock.y+2):
                            foundCollision = False
                            if ((x, y) in area.objList.values()):
                                foundCollision = True
                            if not foundCollision:
                                if random.randrange(0,101) > 35:
                                    flintChance = random.randrange(0,101)
                                    if flintChance > 90:
                                        smallRock = GameObject('o', (80, 80, 80), randx, randy, 'Flint', moveBlock=True)
                                    else:
                                        smallRock = GameObject('o', (153, 102, 0), randx, randy, 'Small-Rock', moveBlock=True)
                                    area.objList[(smallRock.x, smallRock.y)] = smallRock
                else:
                    flintChance = random.randrange(0,101)
                    if flintChance > 90:
                        smallRock = GameObject('o', (80, 80, 80), randx, randy, 'Flint', moveBlock=True)
                    else:
                        smallRock = GameObject('o', (153, 102, 0), randx, randy, 'Small-Rock', moveBlock=True)
                    area.objList[(smallRock.x, smallRock.y)] = smallRock
    
    def generateWater(self, area):
        return
