import pygame
from Maze import Maze

class PgUI:
    def __init__(self, maze, player):
        pygame.font.init()

        self.maze = maze
        self.won = False
        self.font = pygame.font.SysFont('Comic Sans MS', 20)

        self.player = player
        self.OFFSET = 50
        self.TILESIZE = 20
        self.running = True
        self.width = 20
        self.height = 10
        self.screen = pygame.display.set_mode((self.OFFSET * 2 + self.maze.width * self.TILESIZE, self.OFFSET * 2 + self.maze.height * self.TILESIZE))
        pygame.display.set_caption("Maze")
        pygame.draw.rect(self.screen, (255, 255, 255), [self.OFFSET, self.OFFSET,  maze.width * self.TILESIZE,  maze.height * self.TILESIZE], 0)
        self.playerCircle = pygame.draw.circle(self.screen, (255,0,0), (self.OFFSET + self.TILESIZE / 2 + self.player.tilePosition.posX * self.TILESIZE,
                                                                        self.OFFSET + self.TILESIZE / 2 + self.player.tilePosition.posY * self.TILESIZE)
                                                                        , self.TILESIZE/2)
        self.drawUI(maze)

    def restart(self):
        self.won = False
        self.maze.generate()
        self.maze.find_path(self.maze.width - 1, self.maze.height - 1)
        self.player.score = 0
        self.player.moves = 0
        self.player.tilePosition = self.maze.maze[self.maze.STARTX][self.maze.STARTY]
    def drawUI(self, maze):
        if not self.won:
            self.screen.fill((0,0,0))
        else:
            self.screen.fill((0, 175, 0))

        self.movesText = self.font.render("Moves: " + f'{self.player.moves}', False, (255, 255, 255))
        self.screen.blit(self.movesText, (0, 20))

        self.shortestMovesText = self.font.render("Can be solved in " + f'{len(self.maze.path)}' + ' moves', False, (255, 255, 255))
        self.screen.blit(self.shortestMovesText, (0, self.OFFSET + self.TILESIZE * maze.height))

        pygame.draw.rect(self.screen, (255, 255, 255),
                         [self.OFFSET, self.OFFSET, self.maze.width * self.TILESIZE, self.maze.height * self.TILESIZE],
                         0)
        for y in range(0, maze.height):
            for x in range(0, maze.width):
                print(maze.maze[y][x])
                if maze.maze[y][x].rightNode == None:
                    pygame.draw.line(self.screen, (0,0,0), (self.OFFSET + (x + 1) * self.TILESIZE, self.OFFSET + y * self.TILESIZE), (self.OFFSET + (x + 1) * self.TILESIZE, self.OFFSET + (y + 1) * self.TILESIZE))
                if maze.maze[y][x].downNode == None:
                    pygame.draw.line(self.screen, (0,0,0), (self.OFFSET + x * self.TILESIZE, self.OFFSET + (y + 1) * self.TILESIZE), (self.OFFSET + (x + 1) * self.TILESIZE, self.OFFSET + (y + 1) * self.TILESIZE))
        self.playerCircle = pygame.draw.circle(self.screen, (255, 0, 0), (
        self.OFFSET + self.TILESIZE / 2 + self.player.tilePosition.posX * self.TILESIZE,
        self.OFFSET + self.TILESIZE / 2 + self.player.tilePosition.posY * self.TILESIZE)
                                               , self.TILESIZE / 2)
        if self.player.check_win() and not self.won:
            self.won = True
            self.player.calc_score()
        else:
            self.scoreText = self.font.render("Score: " + f'{self.player.score}', False, (255, 255, 255))
            self.screen.blit(self.scoreText, (0, 0))

        pygame.display.flip()


    def continue_display(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    print("key pressed")
                    if event.key == pygame.K_UP:
                        self.player.try_move("UP")
                        print("UP")
                    if event.key == pygame.K_DOWN:
                        self.player.try_move("DOWN")
                        print("DOWN")
                    if event.key == pygame.K_LEFT:
                        self.player.try_move("LEFT")
                        print("LEFT")
                    if event.key == pygame.K_RIGHT:
                        self.player.try_move("RIGHT")
                        print("RIGHT")
                    if event.key == pygame.K_r:
                        self.restart()
            self.drawUI(self.maze)







