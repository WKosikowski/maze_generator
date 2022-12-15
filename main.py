from mazeFrame import MazeFrame
from tkinter import Tk
from Maze import Maze
XBOUND = 5
YBOUND = 7
STARTY = 0
STARTX = 0



def main():
    maze = Maze(YBOUND, XBOUND, STARTY, STARTX)
    maze.generate()
    # for i in range(0, 5):
    #     # maze.maze[i][0].setDownNode(maze.maze[i+1][0])
    #     maze.maze[i][0].rightNode = maze.maze[i][1]
    # print(maze)

    root = Tk()
    ex = MazeFrame(maze)
    root.geometry("400x250+300+300")
    root.mainloop()


main()