from mazeFrame import MazeFrame
from tkinter import Tk
from Maze import Maze
from pyGame import PgUI
from Player import Player
# XBOUND =5
# YBOUND = 5
# STARTY = 0
# STARTX = 0



def main():
    maze = Maze()
    maze.generate()
    maze.find_path(maze.width - 1, maze.height - 1)

    player = Player(maze.maze[maze.STARTX][maze.STARTY], maze)

    # root = Tk()
    # ex = MazeFrame(maze)
    # root.geometry(f'{ex.NODE_SIZE * maze.width + ex.OFFSET * 2}x{ex.NODE_SIZE * maze.height + ex.OFFSET * 2}+30+30')
    # root.mainloop()

    pg_ui = PgUI(maze, player)
    pg_ui.continue_display()
main()