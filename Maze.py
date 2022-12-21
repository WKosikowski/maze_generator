import random
from Tile import Tile


class Maze:
    def __init__(self, yBound = 5, xBound = 5, startY = 0, startX = 0):
        self.height = yBound
        self.width = xBound
        self.STARTX = startX
        self.STARTY = startY
        self.maze = []
        self.path = []




    def get_unvisited_neighbour(self, node):

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


    def link(self, nextNode, originNode):
        if originNode.posX == nextNode.posX:
            if originNode.posY < nextNode.posY:
                originNode.downNode = nextNode
                nextNode.upNode = originNode
                # print("movedTo " + "Down")
            elif originNode.posY > nextNode.posY:
                originNode.upNode = nextNode
                nextNode.downNode = originNode
                # print("movedTo " + "Up")
        elif originNode.posY == nextNode.posY:
            if originNode.posX < nextNode.posX:
                originNode.rightNode = nextNode
                nextNode.leftNode = originNode
                # print("movedTo " + "Right")
            if originNode.posX > nextNode.posX:
                originNode.leftNode = nextNode
                nextNode.rightNode = originNode
                # print("movedTo " + "Left")

    def reset(self):
        self.maze = []
        self.path = []
        for y in range(0, self.height):
            row = []
            for x in range(0, self.width):
                row.append(Tile(y, x))
            self.maze.append(row)
        print(self.maze)

    def generate(self):
        self.reset()

        self.path.append(self.maze[self.STARTY][self.STARTX])
        i = 0
        while len(self.path) > 0:
            current = self.path[len(self.path) - 1]
            current.visited = True
            current_y = current.posY
            current_x = current.posX
            i = i + 1
            # print(i, current_x, current_y)
            nextNode = self.get_unvisited_neighbour(current)
            if nextNode != None:
                self.link(nextNode, current)

                self.path.append(nextNode)

            else:
                self.path.remove(current)




    def find_path(self, findX, findY):
        current = self.maze[self.STARTY][self.STARTX]
        past_nodes = [self.maze[self.STARTY][self.STARTX]]
        while current.posX != findX or current.posY != findY:
            next_node = current.get_neighbours(current)
            if next_node is not None:
                past_nodes.append(next_node)
                current = next_node
            else:
                past_nodes.remove(current)
                current = past_nodes[len(past_nodes) - 1]
        self.path = past_nodes

    def __str__(self) -> str:
        text = 'Maze:[\n'

        for y in self.maze:
            text += '   ['
            for x in y:
                text += str(x) + ' '
            text += ']\n'

        text += ']'
        return text
