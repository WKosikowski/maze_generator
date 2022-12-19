from mazeFrame import MazeFrame
from tkinter import Tk
from Maze import Maze
XBOUND =5
YBOUND = 5
STARTY = 0
STARTX = 0



def main():
    maze = Maze(YBOUND, XBOUND, STARTY, STARTX)
    maze.generate()


    root = Tk()
    ex = MazeFrame(maze)
    root.geometry(f'{ex.NODE_SIZE * XBOUND + ex.OFFSET * 2}x{ex.NODE_SIZE * YBOUND + ex.OFFSET * 2}+30+30')
    root.mainloop()


main()