from tkinter import Canvas, Frame, BOTH
from Maze import Maze
from Node import Node

class MazeFrame(Frame):


    def __init__(self, maze):
        super().__init__()
        self.OFFSET = 30
        self.NODE_SIZE = 20
        self.initUI(maze)

    def initUI(self, maze):
        self.master.title("Lines")
        self.pack(fill=BOTH, expand=10)
        canvas = Canvas(self)
        canvas.create_line(30, 30, 30 + maze.width * 20, 30, 30 + maze.width * 20, 30 + maze.height * 20, 30, 30 + maze.height * 20, 30, 30)

        for y in range(0, maze.height):
            for x in range(0, maze.width):
                print(maze.maze[y][x])
                if maze.maze[y][x].rightNode == None :
                    canvas.create_line((self.OFFSET + (x + 1) * self.NODE_SIZE), (self.OFFSET + y * self.NODE_SIZE), (self.OFFSET + (x + 1) * self.NODE_SIZE), (self.OFFSET + (y + 1) * self.NODE_SIZE))
                if maze.maze[y][x].downNode == None:
                    canvas.create_line((self.OFFSET + x * self.NODE_SIZE), (self.OFFSET + (y + 1) * self.NODE_SIZE), (self.OFFSET + (x + 1) * self.NODE_SIZE), (self.OFFSET + (y + 1) * self.NODE_SIZE))

        canvas.pack(fill=BOTH, expand=1)

