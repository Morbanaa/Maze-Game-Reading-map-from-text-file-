import keyboard

class Player():
    def __init__(self,ypos,xpos):
        self.ypos = ypos
        self.xpos = xpos
        self.score = 0


    def update_player(self,grid):
        bad_tile = {'@'}
        if keyboard.is_pressed("w") and grid[self.ypos -1][self.xpos] not in bad_tile:
            self.ypos -=1
        if keyboard.is_pressed("s") and grid[self.ypos +1][self.xpos] not in bad_tile:
            self.ypos +=1
        if keyboard.is_pressed("a") and grid[self.ypos][self.xpos -1] not in bad_tile:
            self.xpos -=1
        if keyboard.is_pressed("d") and grid[self.ypos][self.xpos +1] not in bad_tile:
            self.xpos +=1

        
