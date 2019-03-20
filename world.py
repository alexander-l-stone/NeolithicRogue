import tcod
import random

class World:
    def __init__(self, seed):
        self.loaded_areas = {}
        self.features = {}
        self.generated_areas = {}
        self.seed = seed
        random.seed(self.seed)
        self.rand_state = random.getstate()
        #eventually grab this from a file
        self.biomes = ['savannah', 'desert', 'forest']
    
    def add_area(self, area):
        self.loaded_areas[(area.x, area.y)] = area
        self.generated_areas[(area.x, area.y)] = area.seed
    
    def get_area(self, area, dx, dy):
        key = (area.x + dx, area.y+dy)
        location = self.loaded_areas.get(key)
        if not location:
            location_seed = self.generated_areas.get(key)
        if location:
            return location
        elif location_seed:
            #generate location using seed for that location
            return location_seed
        else:
            return self.generate_new_area(key)
    
    def generate_new_area(self, key):
        random.setstate(self.rand_state)
        

