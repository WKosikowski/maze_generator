import pygame
import pgzero
import math
class Player:
    def __init__(self, startPosition, maze):
        self.tilePosition = None
        self.tilePosition = startPosition
        self.score = 0
        self.maze = maze
        self.moves = 0

    def try_move(self, direction):
        if direction == "UP" and self.tilePosition.upNode is not None:
            self.tilePosition = self.tilePosition.upNode
            self.moves += 1
            print(self.tilePosition.posX, self.tilePosition.posY)
        if direction == "DOWN" and self.tilePosition.downNode is not None:
            self.tilePosition = self.tilePosition.downNode
            self.moves += 1
            print(self.tilePosition.posX, self.tilePosition.posY)
        if direction == "RIGHT" and self.tilePosition.rightNode is not None:
            self.tilePosition = self.tilePosition.rightNode
            self.moves += 1
            print(self.tilePosition.posX, self.tilePosition.posY)
        if direction == "LEFT" and self.tilePosition.leftNode is not None:
            self.tilePosition = self.tilePosition.leftNode
            self.moves += 1
            print(self.tilePosition.posX, self.tilePosition.posY)



    def calc_score(self):
        self.score = math.floor(self.maze.width * self.maze.height * (len(self.maze.path) / self.moves))

    def check_win(self):
        if self.tilePosition.posY == self.maze.height - 1 and self.tilePosition.posX == self.maze.width - 1 :
            return True
