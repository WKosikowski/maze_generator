class Tile:
    def __init__(self, y, x):
        self.visited = False
        self.neighbourNodesVisited = 0
        self.posX = x
        self.posY = y
        self.upNode = None
        self.rightNode = None
        self.leftNode = None
        self.down_node = None

    def get_neighbours(self, tile):
        if tile.upNode is not None:
            if tile.upNode.visited:
                tile.upNode.visited = False
                return tile.upNode
        if tile.down_node is not None:
            if tile.down_node.visited:
                tile.down_node.visited = False
                return tile.down_node
        if tile.rightNode is not None:
            if tile.rightNode.visited:
                tile.rightNode.visited = False
                return tile.rightNode
        if tile.leftNode is not None:
            if tile.leftNode.visited:
                tile.leftNode.visited = False
                return tile.leftNode
        return None

    def __str__(self):
        return '(' + f'{self.posX}' + ',' + f'{self.posY}' + ' ' + f'{self.rightNode is not None}' + ' ' + f'{self.down_node is not None}' + ')'
