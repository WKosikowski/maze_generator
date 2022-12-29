import math


class Player:
    def __init__(self, startPosition, maze):
        self.tile_position = startPosition
        self.score = 0
        self.maze = maze
        self.moves = 0

    def try_move(self, direction):
        if direction == "UP" and self.tile_position.upNode is not None:
            self.tile_position = self.tile_position.upNode
            self.moves += 1
            print(self.tile_position.posX, self.tile_position.posY)
        if direction == "DOWN" and self.tile_position.down_node is not None:
            self.tile_position = self.tile_position.down_node
            self.moves += 1
            print(self.tile_position.posX, self.tile_position.posY)
        if direction == "RIGHT" and self.tile_position.rightNode is not None:
            self.tile_position = self.tile_position.rightNode
            self.moves += 1
            print(self.tile_position.posX, self.tile_position.posY)
        if direction == "LEFT" and self.tile_position.leftNode is not None:
            self.tile_position = self.tile_position.leftNode
            self.moves += 1
            print(self.tile_position.posX, self.tile_position.posY)



    def calc_score(self):
        self.score = math.floor(self.maze.width * self.maze.height * ((len(self.maze.path) - 1) / self.moves))

    def check_win(self):
        if self.tile_position.posY == self.maze.height - 1 and self.tile_position.posX == self.maze.width - 1 :
            return True
