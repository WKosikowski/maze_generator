from tkinter import Canvas, Frame, BOTH
from Maze import Maze
from Tile import Tile

class MazeFrame(Frame):


    def __init__(self, maze):
        super().__init__()
        self.OFFSET = 30
        self.NODE_SIZE = 20
        self.PATHOFFSET = self.OFFSET + self.NODE_SIZE / 2
        self.initUI(maze)

    def initUI(self, maze):
        self.master.title("Maze")
        self.pack(fill=BOTH, expand=10)
        canvas = Canvas(self)
        canvas.create_line(self.OFFSET, self.OFFSET,
                           self.OFFSET + maze.width * self.NODE_SIZE, self.OFFSET,
                           self.OFFSET + maze.width * self.NODE_SIZE, self.OFFSET + maze.height * self.NODE_SIZE,
                           self.OFFSET, self.OFFSET + maze.height * self.NODE_SIZE, self.OFFSET, self.OFFSET)

        for y in range(0, maze.height):
            for x in range(0, maze.width):
                # print(maze.maze[y][x])
                if maze.maze[y][x].rightNode == None :
                    canvas.create_line((self.OFFSET + (x + 1) * self.NODE_SIZE), (self.OFFSET + y * self.NODE_SIZE), (self.OFFSET + (x + 1) * self.NODE_SIZE), (self.OFFSET + (y + 1) * self.NODE_SIZE))
                if maze.maze[y][x].downNode == None:
                    canvas.create_line((self.OFFSET + x * self.NODE_SIZE), (self.OFFSET + (y + 1) * self.NODE_SIZE), (self.OFFSET + (x + 1) * self.NODE_SIZE), (self.OFFSET + (y + 1) * self.NODE_SIZE))
        lineFromNode = maze.path[0]
        for i in maze.path:
            if i is not lineFromNode:
                canvas.create_line((self.PATHOFFSET + (lineFromNode.posX )  * self.NODE_SIZE), (self.PATHOFFSET + lineFromNode.posY * self.NODE_SIZE),
                                   (self.PATHOFFSET + (i.posX ) * self.NODE_SIZE), (self.PATHOFFSET + (i.posY) * self.NODE_SIZE), fill='red')
                lineFromNode = i
        canvas.pack(fill=BOTH, expand=1)


