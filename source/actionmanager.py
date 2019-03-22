def attemptMove(character, area, dx, dy):
    if (character.x+dx, character.y+dy) in area.objList:
        obj = area.objList[(character.x+dx, character.y+dy)]
        if obj.moveBlock:
            print("Returning false because blocked by object")
            return False
    else:
        for animal in area.animalList:
            if (character.x+dx == animal.x) and (character.y+dy == animal.y):
                print("Returning false because blocked by animal")
                return False
    return True
