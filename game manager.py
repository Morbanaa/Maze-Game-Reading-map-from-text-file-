from player import Player
import random

class GameManager():
    def __init__(self):
        self.grid = []
        self.total_coins = 0
        self.victory = False

        in_file = open('text.txt','r')
        for line in in_file:
            row = []
            for char in line:
                if char != "\n":
                    row.append(char)
            self.grid.append(row)

        self.game_height = len(self.grid)
        self.game_width = len(self.grid[0])

        in_file.close()

        self.player = Player(self.game_height//2,self.game_width//2)   

    def finish_map(self):
        bad_tile = {"@"}
        for y in range(self.game_height):
            for x in range(self.game_width):
                rand = random.randint(1,40)
                if rand == 1 and self.grid[y][x] not in bad_tile:
                    self.grid[y][x] = "*"
                    self.total_coins += 1

    def render_world(self,time_passed):

        RED     = "\033[31m"
        GREEN   = "\033[32m"
        YELLOW  = "\033[33m"
        RESET   = "\033[0m"

        # Preps console for next frame of game
        print("\033[H", end="")

        hours = time_passed // 3600
        minutes = (time_passed % 3600) // 60
        seconds = (time_passed % 60)

        print(f"Timer: {hours:<2}: {minutes:<2}. {seconds:<2}")
        print(f"Score: {self.player.score:<20}")

        for y in range(self.game_height):
            for x in range(self.game_width):
                if y == self.player.ypos and x == self.player.xpos:
                    print(f"{GREEN}+{RESET}",end="")
                elif self.grid[y][x] == "*":
                    print(f"{YELLOW}*{RESET}",end="")
                else:
                    print(f"{self.grid[y][x]}",end="")
            print()

        if self.victory == True:
            print("You Win!!!")
    

    def collect_coin(self):
        if self.grid[self.player.ypos][self.player.xpos] == "*":
            self.grid[self.player.ypos][self.player.xpos] = " "
            self.player.score += 1
      
    def did_win(self):
        if self.player.score >= self.total_coins:
            self.victory = True


    def update_game(self):
        self.player.update_player(self.grid)
        self.collect_coin()
        self.did_win()
