import random
from Node import Node


class Maze:
    def __init__(self, yBound, xBound, startY, startX):
        self.height = yBound
        self.width = xBound
        self.STARTX = startX
        self.STARTY = startY
        self.maze = []
        self.history: [Node] = []

        for y in range(0, self.height):
            row = []
            for x in range(0, self.width):
                row.append(Node(y, x))
            self.maze.append(row)
        print(self.maze)

    def randomise(self, y, x):

        randList: [Node] = []
        if x > 0:
            if not self.maze[y][x - 1].visited:
                randList.append("Left")

        if y > 0:
            if not self.maze[y - 1][x].visited:
                randList.append("Up")

        if x + 1 < self.width:
            if not self.maze[y][x + 1].visited:
                randList.append("Right")

        if y + 1 < self.height:
            if not self.maze[y + 1][x].visited:
                randList.append("Down")

        if len(randList) == 1:
            return randList[0]
        elif len(randList) > 1:
            randNum = random.randint(0, len(randList) - 1)

            returning = randList[randNum]
            return returning
        else:
            return "null"

    def link(self, direction, yOrigin, xOrigin):
        if direction == "Right":
            self.maze[yOrigin][xOrigin].rigthNode = self.maze[yOrigin][xOrigin + 1]
            self.maze[yOrigin][xOrigin + 1].leftNode = self.maze[yOrigin][xOrigin]
            print("movedTo " + "Right")
        if direction == "Left":
            self.maze[yOrigin][xOrigin].leftNode = self.maze[yOrigin][xOrigin - 1]
            self.maze[yOrigin][xOrigin - 1].rightNode = self.maze[yOrigin][xOrigin]
            print("movedTo " + "Left")
        if direction == "Down":
            self.maze[yOrigin][xOrigin].downNode = self.maze[yOrigin + 1][xOrigin]
            self.maze[yOrigin + 1][xOrigin].upNode = self.maze[yOrigin][xOrigin]
            print("movedTo " + "Down")
        if direction == "Up":
            self.maze[yOrigin][xOrigin].upNode = self.maze[yOrigin - 1][xOrigin]
            self.maze[yOrigin - 1][xOrigin].downNode = self.maze[yOrigin][xOrigin]
            print("movedTo " + "Up")

    def generate(self):
        self.history.append(self.maze[self.STARTY][self.STARTX])
        i = 0
        while len(self.history) > 0:
            current = self.history[len(self.history) - 1]
            current.visited = True
            currentY = current.posY
            currentX = current.posX
            i = i + 1
            print(i, currentX, currentY)
            direction = self.randomise(currentY, currentX)
            if direction != "null":
                self.link(direction, currentY, currentX)
                if direction == "Up":
                    currentY -= 1
                elif direction == "Left":
                    currentX -= 1
                elif direction == "Down":
                    currentY += 1
                elif direction == "Right":
                    currentX += 1
                # self.link(direction, currentY, currentX)
                self.history.append(self.maze[currentY][currentX])
            else:
                if len(self.history) > 0:
                    del self.history[len(self.history) - 1]

    def __str__(self) -> str:
        text = 'Maze:[\n'

        for y in self.maze:
            text += '   ['
            for x in y:
                text += str(x) + ' '
            text += ']\n'

        text += ']'
        return text
