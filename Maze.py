import random
from Node import Node


class Maze:
    def __init__(self, yBound, xBound, startY, startX):
        self.height = yBound
        self.width = xBound
        self.STARTX = startX
        self.STARTY = startY
        self.maze = []
        self.history = []
        self.path = []

        for y in range(0, self.height):
            row = []
            for x in range(0, self.width):
                row.append(Node(y, x))
            self.maze.append(row)
        print(self.maze)

    def randomise(self, node):

        randList = []
        if node.posX > 0:
            if not self.maze[node.posY][node.posX - 1].visited:
                randList.append(self.maze[node.posY][node.posX - 1])

        if node.posY > 0:
            if not self.maze[node.posY - 1][node.posX].visited:
                randList.append(self.maze[node.posY - 1][node.posX])

        if node.posX < self.width - 1:
            if not self.maze[node.posY][node.posX + 1].visited:
                randList.append(self.maze[node.posY][node.posX + 1])

        if node.posY < self.height - 1:
            if not self.maze[node.posY + 1][node.posX].visited:
                randList.append(self.maze[node.posY + 1][node.posX])

        if len(randList) == 1:
            return randList[0]
        elif len(randList) > 1:
            randNum = random.randint(0, len(randList) - 1)

            returning = randList[randNum]
            return returning
        else:
            return None
    # def randomise(self, y, x):
    #
    #     randList = []
    #     if x > 0:
    #         if not self.maze[y][x - 1].visited:
    #             randList.append("Left")
    #
    #     if y > 0:
    #         if not self.maze[y - 1][x].visited:
    #             randList.append("Up")
    #
    #     if x < self.width - 1:
    #         if not self.maze[y][x + 1].visited:
    #             randList.append("Right")
    #
    #     if y < self.height - 1:
    #         if not self.maze[y + 1][x].visited:
    #             randList.append("Down")
    #
    #     if len(randList) == 1:
    #         return randList[0]
    #     elif len(randList) > 1:
    #         randNum = random.randint(0, len(randList) - 1)
    #
    #         returning = randList[randNum]
    #         return returning
    #     else:
    #         return "null"

    def link(self, nextNode, originNode):
        if originNode.posX == nextNode.posX:
            if originNode.posY < nextNode.posY:
                originNode.downNode = nextNode
                nextNode.upNode = originNode
                print("movedTo " + "Down")
            elif originNode.posY > nextNode.posY:
                originNode.upNode = nextNode
                nextNode.downNode = originNode
                print("movedTo " + "Up")
        elif originNode.posY == nextNode.posY:
            if originNode.posX < nextNode.posX:
                originNode.rightNode = nextNode
                nextNode.leftNode = originNode
                print("movedTo " + "Right")
            if originNode.posX > nextNode.posX:
                originNode.leftNode = nextNode
                nextNode.rightNode = originNode
                print("movedTo " + "Left")


        # if direction == "Right":
        #     self.maze[yOrigin][xOrigin].rightNode = self.maze[yOrigin][xOrigin + 1]
        #     self.maze[yOrigin][xOrigin + 1].leftNode = self.maze[yOrigin][xOrigin]
        #     print("movedTo " + "Right")
        # if direction == "Left":
        #     self.maze[yOrigin][xOrigin].leftNode = self.maze[yOrigin][xOrigin - 1]
        #     self.maze[yOrigin][xOrigin - 1].rightNode = self.maze[yOrigin][xOrigin]
        #     print("movedTo " + "Left")
        # if direction == "Down":
        #     self.maze[yOrigin][xOrigin].downNode = self.maze[yOrigin + 1][xOrigin]
        #     self.maze[yOrigin + 1][xOrigin].upNode = self.maze[yOrigin][xOrigin]
        #     print("movedTo " + "Down")
        # if direction == "Up":
        #     self.maze[yOrigin][xOrigin].upNode = self.maze[yOrigin - 1][xOrigin]
        #     self.maze[yOrigin - 1][xOrigin].downNode = self.maze[yOrigin][xOrigin]
        #     print("movedTo " + "Up")


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
            nextNode = self.randomise(current)
            if nextNode != None:
                self.link(nextNode, current)

                self.history.append(nextNode)
                # if self.history[len(self.history) - 1].posX == self.width - 1 and self.history[len(self.history) - 1].posY == self.height - 1:
                #     self.path = self.history.copy()
                #     print("path assigned" ,f'{self.path}')
                # self.history.append(self.maze[currentY][currentX])
            else:
                self.history.remove(current)
        self.path = self.findPath(4,4)


    def findNeighbours(self, node):
        if node.upNode != None:
            if node.upNode.visited == True:
                node.upNode.visited = False
                return node.upNode
        if node.downNode != None:
            if node.downNode.visited == True:
                node.downNode.visited = False
                return node.downNode
        if node.rightNode != None:
            if node.rightNode.visited == True:
                node.rightNode.visited = False
                return node.rightNode
        if node.leftNode != None:
            if node.leftNode.visited == True:
                node.leftNode.visited = False
                return node.leftNode
        return None

    def findPath(self, findX, findY):
        current = self.maze[self.STARTY][self.STARTX]
        pastNodes = [self.maze[self.STARTY][self.STARTX]]
        while current.posX != findX or current.posY != findY:
            nextNode = self.findNeighbours(current)
            if nextNode != None:
                pastNodes.append(nextNode)
                current = nextNode
            else:
                pastNodes.remove(current)
                current = pastNodes[len(pastNodes) - 1]
        return pastNodes

    def __str__(self) -> str:
        text = 'Maze:[\n'

        for y in self.maze:
            text += '   ['
            for x in y:
                text += str(x) + ' '
            text += ']\n'

        text += ']'
        return text
