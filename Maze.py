import random
from Tile import Tile


class Maze:
    def __init__(self, height=5, width=5, start_y=0, start_x=0):
        self.height = height
        self.width = width
        self.STARTX = start_x
        self.STARTY = start_y
        self.maze = []
        self.path = []

    def get_unvisited_neighbour(self, node):

        rand_list = []
        if node.posX > 0:
            if not self.maze[node.posY][node.posX - 1].visited:
                rand_list.append(self.maze[node.posY][node.posX - 1])

        if node.posY > 0:
            if not self.maze[node.posY - 1][node.posX].visited:
                rand_list.append(self.maze[node.posY - 1][node.posX])

        if node.posX < self.width - 1:
            if not self.maze[node.posY][node.posX + 1].visited:
                rand_list.append(self.maze[node.posY][node.posX + 1])

        if node.posY < self.height - 1:
            if not self.maze[node.posY + 1][node.posX].visited:
                rand_list.append(self.maze[node.posY + 1][node.posX])

        if len(rand_list) == 1:
            return rand_list[0]
        elif len(rand_list) > 1:
            rand_num = random.randint(0, len(rand_list) - 1)

            returning = rand_list[rand_num]
            return returning
        else:
            return None

    def link(self, next_node, origin_node):
        if origin_node.posX == next_node.posX:
            if origin_node.posY < next_node.posY:
                origin_node.down_node = next_node
                next_node.upNode = origin_node
                # print("movedTo " + "Down")
            elif origin_node.posY > next_node.posY:
                origin_node.upNode = next_node
                next_node.down_node = origin_node
                # print("movedTo " + "Up")
        elif origin_node.posY == next_node.posY:
            if origin_node.posX < next_node.posX:
                origin_node.rightNode = next_node
                next_node.leftNode = origin_node
                # print("movedTo " + "Right")
            if origin_node.posX > next_node.posX:
                origin_node.leftNode = next_node
                next_node.rightNode = origin_node
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
            # current_y = current.posY
            # current_x = current.posX
            i = i + 1
            # print(i, current_x, current_y)
            next_node = self.get_unvisited_neighbour(current)
            if next_node is not None:
                self.link(next_node, current)
                self.path.append(next_node)
            else:
                self.path.remove(current)

    def find_path(self, find_x, find_y):
        current = self.maze[self.STARTY][self.STARTX]
        past_nodes = [self.maze[self.STARTY][self.STARTX]]
        while current.posX != find_x or current.posY != find_y:
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
