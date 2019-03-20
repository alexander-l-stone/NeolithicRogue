class GameObject:
    def __init__(self, char, color, x, y, name, visionBlock=False, moveBlock=False, bgcolor=None):
        self.char = char
        self.color = color
        self.x = x
        self.y = y
        self.bgcolor = bgcolor
        self.visionBlock = visionBlock
        self.moveBlock = moveBlock

    def draw(self, console, topx, topy, sw, sh):
        if (self.x-topx > 0) and (self.y-topy > 0) and (self.x-topx < sw) and (self.y-topy < sh):
            console.draw_char(self.x-topx, self.y-topy, self.char, self.color, bg=self.bgcolor)

    def clear(self, console, topx, topy, sw, sh, clearbg=None):
        if (self.x-topx > 0) and (self.y-topy > 0) and (self.x-topx < sw) and (self.y-topy < sh):
            console.draw_char(self.x-topx, self.y-topy, ' ', bg=clearbg)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class Tile:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def draw(self, console, topx, topy, sw, sh):
        if (self.x-topx > 0) and (self.y-topy > 0) and (self.x-topx < sw) and (self.y-topy < sh):
            console.draw_char(self.x-topx, self.y-topy, ' ', self.color, bg=self.color)

    def clear(self, console, topx, topy, sw, sh, clearbg=None):
        if (self.x-topx > 0) and (self.y-topy > 0) and (self.x-topx < sw) and (self.y-topy < sh):
            console.draw_char(self.x-topx, self.y-topy, ' ', bg=clearbg)
