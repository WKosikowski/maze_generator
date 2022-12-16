from mazeFrame import MazeFrame
from tkinter import Tk
from Maze import Maze
XBOUND =45
YBOUND = 52
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
    root.geometry(f'{ex.NODE_SIZE * XBOUND + ex.OFFSET * 2}x{ex.NODE_SIZE * YBOUND + ex.OFFSET * 2}+30+30')
    root.mainloop()


main()