from mazeFrame import MazeFrame
from tkinter import Tk
from Maze import Maze
# XBOUND =5
# YBOUND = 5
# STARTY = 0
# STARTX = 0



def main():
    maze = Maze()
    maze.generate()
    maze.find_path(maze.width - 1, maze.height - 1)


    root = Tk()
    ex = MazeFrame(maze)
    root.geometry(f'{ex.NODE_SIZE * maze.width + ex.OFFSET * 2}x{ex.NODE_SIZE * maze.height + ex.OFFSET * 2}+30+30')
    root.mainloop()


main()